# Import necessary modules
import pandas as pd
from bs4 import BeautifulSoup

# Function to get Twitter data from a CSV file
def get_twitter_data():
    # Read data from 'twitter_bookmarks.csv' into a DataFrame
    df = pd.read_csv("twitter_bookmarks_example.csv")    
    
    # Drop rows where all columns are NaN
    df.dropna(how='all', inplace=True)
    
    # Add a 'Source' column with the value 'Twitter' to the DataFrame
    df['Source'] = 'Twitter'
    
    # Return the DataFrame with Twitter data
    return df

# Function to get Reddit data from an HTML file
def get_reddit_data():
    # Open and read the 'reddit_saved_posts.html' file
    with open("reddit_saved_posts_example.html", "r", encoding="utf-8") as file:
        html = file.read()
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    
    # Initialize an empty list to store Reddit data
    data = []
    current_h2 = None

    # Loop through all 'h2' and 'li' elements in the HTML
    for element in soup.find_all(['h2', 'li']):
        if element.name == 'h2':
            # If the element is an 'h2', set current_h2 to its text
            current_h2 = element.text
        elif element.name == 'li' and current_h2 is not None:
            # If the element is an 'li' and we have a current_h2 value
            # Extract post content and link information
            post_content = element.a.text
            post_link = element.a['href']
            data.append([current_h2, post_content, post_link])
    
    # Create a DataFrame from the collected data
    df = pd.DataFrame(data, columns=["Category", "Post Content", "Post Link"])
    
    # Add a 'Source' column with the value 'Reddit' to the DataFrame
    df['Source'] = 'Reddit'
    
    # Return the DataFrame with Reddit data
    return df
