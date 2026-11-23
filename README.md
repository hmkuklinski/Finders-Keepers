# Finders-Keepers


Finders Keepers is a Flask application that utilizes the EXA API to generate suggestive content for users based on the search parameters. The User Interface makes it easy for users to search for their favorite topics on various platforms - TikTok, Twitter/X, and Instagram.

![Screenshot 2024-05-28 031713](https://github.com/hmkuklinski/Finders-Keepers/assets/143479397/4349c45d-3de9-43c3-9351-dce61492de82)

## Setup- Get EXA API KEY
Finders Keepers uses [Exa](https://exa.ai/) to search the web and retrieve content previews.

1. Visit [Exa](https://exa.ai/) and create an account.
2. Navigate to the [Exa Dashboard](https://dashboard.exa.ai/).
3. Generate an API key from your dashboard.
4. Create a `.env` file in the project's root directory.
5. Add your API key and Flask session key:

   ```env
   API_KEY=your_exa_api_key
   SESSION_KEY=your_secret_session_key
   ```

**Important:** Keep your API key private. Never commit your `.env` file to GitHub. Make sure `.env` is included in your `.gitignore` file.

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd search-engine
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   **Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **Mac/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure environment variables by creating a `.env` file in the project root:
   ```env
   EXA_API_KEY=your_api_key
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open the application in your browser at `http://127.0.0.1:5000`.

### Deactivating the Virtual Environment

When finished, deactivate the virtual environment:
```bash
deactivate
```

## How to Use:
The user will first type in their desired search topic, followed by the number of searches they would like returned (with a maximum of 7). The user will then select one of the three search options and click the green search button to generate results.

![Screenshot 2024-05-28 031744](https://github.com/hmkuklinski/Finders-Keepers/assets/143479397/cba3859c-665d-4093-9ef3-72b03d2e4529)

## Possible Results: TikTok
The TikTok results can display: suggested user profiles, a discovery tag, or a suggested video.

### Suggested Creator/Account:

![Screenshot 2024-05-28 031834](https://github.com/hmkuklinski/Finders-Keepers/assets/143479397/f1299a84-56f3-4eec-a00d-66351ee16371)

If you would like to visit the creator's account profile in TikTok, click on the embedded profile name.

### Video Preview:


![Screenshot 2024-05-26 012701](https://github.com/hmkuklinski/Finders-Keepers/assets/143479397/cf332b0f-fd3b-4010-bcfa-a604060f778d)

The embedded video will automatically start once it is fully loaded. If you would like to open the video in the TikTok app (either to like, comment, or save it), click the video and it will pop up in a new window.


### Discovery Tag 

![Screenshot 2024-05-28 032119](https://github.com/hmkuklinski/Finders-Keepers/assets/143479397/4054300f-167a-46b4-baae-c279dc7eccdd)

(disclaimer) Due to embedding issues with TikTok discovery tags, the user will be prompted to click on the discover image to open the discover tag link in a separate window. Unfortunately no preview of the discovery tag will be shown.



## Possible Results: Twitter/X

### User Timeline Preview:

![Screenshot](https://firebasestorage.googleapis.com/v0/b/codedex-io.appspot.com/o/community%2Fproject-showcase%2Fpost%2Fmb577tJgITTUF2Zyexr4%2FScreenshot%202024-05-28%20032844.png?alt=media&token=5df8cad5-e34f-4e06-8ed8-9527059b4388)

The user will be able to see the posts from an account using the scroll bar. If you would like to view the account, click on the username of the account in the feed.

### User Post:

![Screenshot 2024-05-28 032902](https://github.com/hmkuklinski/Finders-Keepers/assets/143479397/36c29f2b-88a6-4872-a4c4-b16eacfde99a)

It will sometimes suggest a single tweet that it thinks the user might like. 


## Possible Results: Instagram
![Screenshot](https://firebasestorage.googleapis.com/v0/b/codedex-io.appspot.com/o/community%2F30-nites-of-code%2Fpost%2FDsRLoXKqLleHW4g4OZap%2FScreenshot%202024-05-28%20023720.png?alt=media&token=6e221e21-19fc-4780-9607-b1b93a2ef248)

The instagram link will mainly suggest accounts for the users to follow. The user will be able to see a preview of the user's past posts.

### User Post:
It will sometimes suggest a single post that it thinks the user might like. 
