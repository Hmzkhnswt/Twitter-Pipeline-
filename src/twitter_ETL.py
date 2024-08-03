import tweepy 
import pandas as pd
import json
from datetime import datetime
import s3fs
from dotenv import load_dotenv
import os

load_dotenv("./Twitter-Pipeline-/.env")

access_key = os.getenv()
access_secret = os.getenv()
consumer_key = os.getenv()
consumer_secret = os.getenv()