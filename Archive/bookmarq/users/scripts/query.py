import os
import django
from users.models import CustomUser
from allauth.socialaccount.models import SocialToken, SocialAccount
import requests
import json


# Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learn_easy.settings")

# Initialize Django
django.setup()

def get_bookmarks(access_token, refresh_token, user_id):
    print("Getting Bookmarks!")
    usernames = "usernames=TwitterDev,TwitterAPI"
    user_fields = "user.fields=description,created_at"
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    headers = {
    "Authorization": "Bearer {}".format(access_token),
    "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers)

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )
    json_response = response.json()

    # return requests.request(
    #     "POST",
    #     "https://api.twitter.com/2/tweets",
    #     json=payload,
    #     headers={
    #         "Authorization": "Bearer {}".format(token["access_token"]),
    #         "Content-Type": "application/json",
    #     },
    # )

def get_token():
    account_id_to_lookup = 1
    social_account_access_token = SocialToken.objects.get(account_id=account_id_to_lookup).token
    social_account_refresh_token = SocialToken.objects.get(account_id=account_id_to_lookup).token_secret
    social_account_uid = SocialAccount.objects.get(pk=account_id_to_lookup).uid
    response = get_bookmarks(social_account_access_token, social_account_refresh_token, social_account_uid)

def run():
    get_token()