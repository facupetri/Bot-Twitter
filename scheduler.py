
import time
import random
import os
import logging
from datetime import datetime
import csv
import tweepy
from config import api_key, api_key_secret, access_token, access_token_secret

# Logger configuration
logger = logging.getLogger("tweet_logger")
logger.setLevel(logging.INFO)

# Log to file
file_handler = logging.FileHandler("tweet_log.txt")
file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"))

# Log to console
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(message)s"))

# Avoid duplicate handlers
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Authentication
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Read CSV content
def load_posts():
    with open("posts.csv", newline='', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        return reader

# Post a random tweet
def publish_tweet():
    logger.info("Attempting to publish tweet...")
    posts = load_posts()
    post = random.choice(posts)

    text = post["text"].strip()
    image = post.get("image", "").strip()

    try:
        if image:
            media_path = os.path.join("media", image)
            if not os.path.exists(media_path):
                logger.warning(f"Image not found: {media_path}. Publicando solo texto.")
                api.update_status(status=text)
                logger.info(f"Published text only: {text}")
                return
            media = api.media_upload(media_path)
            api.update_status(status=text, media_ids=[media.media_id])
            logger.info(f"Published with image: {text}")
        else:
            api.update_status(status=text)
            logger.info(f"Published text only: {text}")

    except Exception as e:
        logger.error(f"Error while publishing: {e}")

# Loop with interval (e.g. every 3 hours)
while True:
    publish_tweet()
    logger.info("Waiting 3 hours for the next post...\n")
    time.sleep(3 * 60 * 60)  # 3 hours in seconds
