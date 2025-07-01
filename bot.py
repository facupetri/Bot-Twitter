import tweepy

from config import api_key, api_key_secret, access_token, access_token_secret, bearer_token

# Authentication using OAuth1
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

try:
    user = api.verify_credentials()
    print(f"Conected as: @{user.screen_name}")
except Exception as e:
    print("Authentication failed", e)
