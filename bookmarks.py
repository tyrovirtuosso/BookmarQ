# Import necessary libraries and modules
from utils import get_reddit_data, get_twitter_data
import pandas as pd

# Get Twitter and Reddit data using the functions from utils
twitter_df = get_twitter_data()
reddit_df = get_reddit_data()

# Create a new DataFrame to combine both Twitter and Reddit data
combined_df = pd.DataFrame()

# Normalize Twitter data by selecting specific columns
# Twitter data columns are: 'Source', 'Posted By', 'Content', and 'Tweet URL'
combined_df['Source'] = twitter_df['Source']
combined_df['Posted By'] = twitter_df['Posted By']
combined_df['Content'] = twitter_df['Content']
combined_df['Link'] = twitter_df['Tweet URL']

# Normalize Reddit data by selecting specific columns
# Reddit data columns are: 'Source', 'Category', 'Post Content', and 'Post Link'
reddit_combined = pd.DataFrame()
reddit_combined['Source'] = reddit_df['Source']
reddit_combined['Posted By'] = reddit_df['Category']
reddit_combined['Content'] = reddit_df['Post Content']
reddit_combined['Link'] = reddit_df['Post Link']

# Concatenate the two DataFrames to combine Twitter and Reddit data
combined_df = pd.concat([combined_df, reddit_combined], ignore_index=True)

# Create a dictionary to map Twitter-specific field names to new names
# This will help organize Twitter-specific data within the combined DataFrame
twitter_specific_fields = {
    'Tweet Date': 'Tweet Date',
    'Posted By Profile Pic': 'Profile Pic',
    'Posted By Profile URL': 'Profile URL',
    'Posted By Twitter Handle': 'Twitter Handle',
    'Tags': 'Tags',
    'Comments': 'Comments',
    'Media': 'Media'
}

# Create a new column 'Metadata' in the combined DataFrame to store Twitter-specific fields as dictionaries
combined_df['Metadata'] = twitter_df[twitter_specific_fields.keys()].apply(lambda row: row.to_dict(), axis=1)

# Save the combined DataFrame to a CSV file
combined_df.to_csv('combined_bookmarks.csv', index=False)
