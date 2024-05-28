from exa_py import Exa
from dotenv import load_dotenv
from flask import Flask, render_template, e
import os

#------------------- NOTE: this is python only version/not connected to finders keepers project ------------
#for the API key stored elsewhere
load_dotenv()
API_KEY = os.getenv('API_KEY')

#need to pass in API key into Exa()
exa= Exa(API_KEY)  

while True:
    try:
        #gets input of what user wants to search and stores in query variable
        query = input('\nSearch Topic: ')
        
        #how many results would the user like to see?:
        user_results = int(input("How many results would you like to see?: "))
        
        #ask user where they'd like to search:
        search_location_input = int(input("\nWhere would you like to search?: \n1)TikTok \n2)Twitter \n3)Pinterest\n"))
        
        #change destination based on user's selection--> default to TikTok
        if search_location_input == 1:
            search_location = 'https://www.tiktok.com'
        elif search_location_input == 2:
            search_location = 'https://www.twitter.com'
        elif search_location_input == 3:
            search_location ='https://www.pinterest.com'
        else:
            print("\nNumber not provided in possible selections. The default search will be on TikTok")
            search_location = 'https://www.tiktok.com'
        
        #API call:
        response= exa.search(
            query,
            num_results=user_results,
            type='keyword',
            include_domains=[search_location]
        )
        
        #response format: Title, URL, ID, Score, Published Data, Author, Highlights, Highlights Score

        #want to print only the title and the URL we can access it
        for result in response.results:
            print(f'Title: {result.title}') #name of the video/post 
            print(f'URL: {result.url}\n') #the URL of the post
        
        #perform another search?
        print("Would you like to start another search?")
        another_search = input("Type Yes or No\n")
        
        #exits program only if user types no- any other input, will repeat
        if another_search.lower() == 'no':
            break
        
    #user tries typing out the location they'd like to check instead of number:   
    except ValueError:
        print("Invalid input. Please type a number 1-3")



