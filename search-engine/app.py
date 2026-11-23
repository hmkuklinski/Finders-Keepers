from flask import Flask, render_template, request, redirect, url_for, session
from exa_py import Exa
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
from html.parser import HTMLParser
from uuid import uuid4
import os
import re
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

exa = Exa(API_KEY)
app = Flask(__name__)
app.secret_key = os.getenv('SESSION_KEY')

# Temporary storage for search results.
search_cache = {}


# Get Metadata from websites
class MetadataParser(HTMLParser):
    """Extract Open Graph images and descriptions from a webpage."""

    def __init__(self):
        super().__init__()
        self.metadata = {}

    def handle_starttag(self, tag, attrs):
        if tag != 'meta':
            return
        attrs = dict(attrs)
       
        key = attrs.get('property') or attrs.get('name')
        value = attrs.get('content')
        if key and value:
            self.metadata[key.lower()] = value


def get_website_metadata(url):
    """Retrieve a website's Open Graph metadata."""
    metadata = {
        'image': None,
        'description': None
    }

    try:
        response = requests.get(
            url,
            headers={'User-Agent': 'Mozilla/5.0'},
            timeout=5
        )
        response.raise_for_status()
        parser = MetadataParser()
        parser.feed(response.text)

        # extract Open Graph and Twitter metadata if available
        metadata['image'] = (
            parser.metadata.get('og:image')
            or parser.metadata.get('twitter:image')
        )
        metadata['description'] = (
            parser.metadata.get('og:description')
            or parser.metadata.get('description')
            or parser.metadata.get('twitter:description')
        )

    except requests.RequestException as e:
        print(f"Could not retrieve website metadata for {url}: {e}")

    return metadata


# YouTube ID Extraction
def get_youtube_id(url):
    """Extract a YouTube video ID from supported URL formats."""

    parsed = urlparse(url)

    if parsed.hostname in ('youtu.be', 'www.youtu.be'):
        return parsed.path.strip('/').split('/')[0]

    if parsed.hostname and 'youtube.com' in parsed.hostname:
        if parsed.path == '/watch':
            return parse_qs(parsed.query).get('v', [None])[0]

        match = re.match(r'^/(?:embed|shorts)/([^/?]+)', parsed.path)
        if match:
            return match.group(1)

    return None


def get_preview(url, title, description=''):
    """Identify the content type and prepare its preview information."""

    parsed = urlparse(url)
    domain = (parsed.hostname or '').lower()
    path = parsed.path.strip('/')

    preview = {
        'type': 'website',
        'embed_url': None,
        'thumbnail_url': None,
        'embed_html': None,
        'description': description
    }

    # YouTube
    youtube_id = get_youtube_id(url)

    if youtube_id:
        preview['type'] = 'youtube'
        preview['embed_url'] = (f'https://www.youtube-nocookie.com/embed/{youtube_id}')
        preview['thumbnail_url'] = (f'https://img.youtube.com/vi/{youtube_id}/hqdefault.jpg')
        return preview

    # Spotify
    if domain.endswith('spotify.com'):
        parts = path.split('/')

        if len(parts) >= 2 and parts[0] in ('artist', 'album', 'track', 'playlist', 'episode', 'show'):
            preview['type'] = 'spotify'
            preview['embed_url'] = (f'https://open.spotify.com/embed/{parts[0]}/{parts[1]}')
            return preview

    # TikTok
    if domain.endswith('tiktok.com'):
        preview['type'] = 'tiktok'

        try:
            response = requests.get(
                'https://www.tiktok.com/oembed',
                params={'url': url},
                timeout=5
            )
            response.raise_for_status()
            preview['embed_html'] = response.json().get('html')

        except (requests.RequestException, ValueError) as e:
            print(f"TikTok preview unavailable: {e}")

        return preview

    # Instagram
    if domain.endswith('instagram.com'):
        preview['type'] = 'instagram'
        return preview

    # X / Twitter
    if domain.endswith(('x.com', 'twitter.com')):
        if '/status/' in url:
            preview['type'] = 'twitter'
        else:
            preview['type'] = 'profile'

        return preview

    # General websites
    metadata = get_website_metadata(url)

    preview['thumbnail_url'] = metadata['image']

    if metadata['description']:
        preview['description'] = metadata['description']

    return preview

# Home route
@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        user_results = int(request.form.get('user_results', 10))

        # if no results, return to home page
        if not query:
            return redirect(url_for('home'))

        results = []

        try:
            # Search without domain restrictions.
            response = exa.search(
                query=query,
                num_results=user_results,
                type='keyword'
            )

            # Display search information for debugging
            print('\n--- EXA SEARCH ---')
            print('Query:', query)
            print('Number of results:', len(response.results))

            # Retrieve page text for descriptions.
            urls = [result.url for result in response.results]
            content_by_url = {}

            if urls:
                try:
                    contents = exa.get_contents(urls, text=True)

                    for content in contents.results:
                        content_by_url[content.url] = (content.text or '')

                except Exception as e:
                    print('Could not retrieve page content:', repr(e))

            # Build preview information for each result.
            for result in response.results:

                page_text = content_by_url.get(result.url, '')
                description = ' '.join(page_text.split())[:200]
                preview = get_preview(result.url, result.title, description)

                results.append(
                    {
                        'title': result.title or result.url,
                        'url': result.url,
                        'description': preview['description'],
                        'preview_type': preview['type'],
                        'embed_url': preview['embed_url'],
                        'thumbnail_url': preview['thumbnail_url'],
                        'embed_html': preview['embed_html']
                    }
                )

        except Exception as e:
            print('Search error:', repr(e))

        search_id = str(uuid4())
        search_cache[search_id] = results

        session['search_id'] = search_id
        session['query'] = query

        return redirect(url_for('results'))

    return render_template('index.html')

# Results route
@app.route('/results')
def results():

    search_id = session.get('search_id')
    results = search_cache.get(search_id, [])

    # return to home if no results are found
    if not results:
        return redirect(url_for('home'))

    # display results page with search results
    return render_template(
        'results.html',
        results=results,
        total_results=len(results),
        query=session.get('query', '')
    )


if __name__ == '__main__':
    app.run(debug=True)