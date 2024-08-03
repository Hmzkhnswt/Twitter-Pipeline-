import tweepy 
import pandas as pd
import json
from datetime import datetime
import s3fs
from dotenv import load_dotenv
import os

load_dotenv('/Users/mac/Desktop/Hamza Ali/Twitter-Pipeline-/.env')

access_key = os.getenv("API_KEY")
access_secret = os.getenv("API_KEY_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("ACCESS_TOKEN")
consumer_secret = os.getenv("ACCESS_TOKEN_SECRET")

def run_twitter_etl():
    # Authentication of the twitter:
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name='@babarazam258', 
                            count=200,
                            include_rts = False,
                            tweet_mode = 'extended')

    tweets_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        tweets_list.append(refined_tweet)

    df = pd.DataFrame(tweets_list)
    df.to_csv('s3://twitter-etl-data/refined_tweets.csv')