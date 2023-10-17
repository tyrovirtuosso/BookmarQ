# BookmarQ

## Overview

The BookmarQ project was initially created to automatically fetch 'Bookmarks' and 'Saved Posts' from Twitter (now 'X') and Reddit. However, due to changes in the Twitter API, particularly the cost associated with API access ($100 per month), this approach became impractical. We had implemented social login for Twitter using Django to obtain the required OAuth tokens for the API, but it was eventually archived to the 'Archive' folder.

## New Approach

In light of the challenges with Twitter, I explored alternative methods for managing thousands of bookmarks and saved posts across Twitter and Reddit. I found that the optimal solution is to use [dewey's X sidebar](https://getdewey.co/) to sync all bookmarks and export them as a CSV. It's important to note that for exporting more than 20 bookmarks, you'll need to purchase a plan. In my case, I purchased the monthly plan for $10, used it to export my bookmarks, and then canceled the subscription. The sidebar extension feature is particularly useful for filtering bookmarks within the Twitter app, and dewey provides a dashboard for organizing all your bookmarks. I suggest you take a look at it!

For Reddit, I used [RedditManager](https://redditmanager.com/app#). This tool offers an "Export all items" option, which generates an .html file containing all the saved posts. Additionally, the app itself is handy for browsing through saved posts.

## Implementation

The core functionality of the project is implemented in the `bookmarks.py` script, which fetches data and normalizes it into a CSV based on common fields. Twitter has a few additional fields, which are included as a dictionary in the Metadata field.

## Get Involved

If you discover a more straightforward or cost-effective way to access Twitter Bookmarks or have suggestions for improving this project, please don't hesitate to reach out and let me know. I'm open to contributions and enhancements!
