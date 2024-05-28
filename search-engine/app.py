from flask import Flask, render_template, request, redirect, url_for, session
from exa_py import Exa
from dotenv import load_dotenv
import os, requests

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Initialize the Exa object with the API key
exa = Exa(API_KEY)

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_KEY')

def embed_content(vid_url, loc):
    #note: pass in search_location_input for loc (number value stored for each option clicked)
    # 1- tiktok, 2- twitter, 3-instagram
    
    # loc 1 == 'tiktok'
    if loc == '1':
        params = {
            'url': vid_url,
            'maxwidth': 200,
            'maxheight': 200
            } #need tiktok url to pass as param for requests
        response = requests.get('https://www.tiktok.com/oembed', params=params) #need to make request to oEmbed API to fetch HTML for tiktok vid
        embed_html = response.json().get('html', '') #grab HTML from JSON
        if '/video/' in vid_url:
            embed_class= 'tiktok-vid'
        elif '/tag/' in vid_url:
            embed_class='tiktok-tag'
        else:
            embed_class='tiktok-profile'
    # loc 2 == 'twitter'
    elif loc == '2':
        #this is a tweet that we can embed:
        if '/status/' in vid_url:
            tweet_id = vid_url.split('/')[-1]  # Extract tweet ID from the tweet URL
            tweet_url = f"https://twitter.com/Twitter/status/{tweet_id}"  # Construct tweet URL
            embed_html = f'<blockquote class="twitter-tweet"><a href="{tweet_url}"></a></blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
            embed_class = 'tweet-preview'
        #this is a user profile suggestion:
        else:
            profile_url = vid_url
            embed_html = f'<a class="twitter-timeline" href="{profile_url}?ref_src=twsrc%5Etfw">Tweets by {profile_url.split("/")[-1]}</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
            embed_class = 'twitter-profile'

    # loc 3 == 'instagram'
    elif loc == '3':
        embed_html = f'<blockquote class="instagram-media" data-instgrm-permalink="{vid_url}" data-instgrm-version="13"></blockquote><script async src="//www.instagram.com/embed.js"></script>'
        embed_class= 'insta-preview'
    else:
        # Default case or handle other platforms
        embed_html = f'<div>No embed available for platform: {loc}</div>'
        embed_class = 'unknown'
    return {'html': embed_html, 'class': embed_class}



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': #user clicks submit button
        query = request.form['query'] #search for the 'query' --> get user's desired topic
        user_results = int(request.form['user_results']) # number of results user wants to see
        search_location_input = request.form['search_location'] #search_location is name of options/selections (radio)
        # Determine the search location based on the user's selection
        if search_location_input == "1":
            search_location = 'https://www.tiktok.com'
        elif search_location_input == "2":
            search_location = 'https://www.twitter.com'
        elif search_location_input == '3':
            search_location= 'https://www.instagram.com'
        else:
            search_location = 'https://www.tiktok.com'

        # API call
        response = exa.search(
            query=query,
            num_results=user_results,
            type='keyword',
            include_domains=[search_location]
        )
        print(response)

        # Prepare the results to be displayed
        results = []
        for result in response.results: #want to go through each result and create:
            embed_info = embed_content(result.url, search_location_input) 
            results.append({'title': result.title, 'url': result.url, 'embed_html': embed_info['html'], 'embed_class': embed_info['class']})
        
        #session (temp storage across different requests):
        session['results'] = results
        
        #to keep track of total results wanted by user:
        session['total_results'] = len(results)
        
        #redirect to results page to show results:
        return redirect(url_for('results', page=1))
    else:
        return render_template('index.html')
    
@app.route('/results')
def results():
    results= session.get('results',[])
    total_results = len(results)
    results_per_page = 1
    page = int(request.args.get('page', 1))-1
    
    if page<0 or page >= total_results: #keeps in bound of index range!
        return redirect(url_for('results', page=1)) 
    
     # Get the single result for the current page
    page_result = results[page:page + results_per_page]
    
     # Determine if there is a next or previous page
    has_next = (page + results_per_page) < total_results
    has_prev = page > 0
    
    return render_template('results.html', results=page_result,
        page=page+1,
        has_next=has_next,
        has_prev=has_prev)


if __name__ == '__main__':
    app.run(debug=True)
