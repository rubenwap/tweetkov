from TwitterSearch import *
import re
import os
from dotenv import load_dotenv
from modules import tweet2sql as sql


def cleanup_text(text):
    """
    Placeholder to clean up inconsistencies from the main corpus. Not urgent, but needs to be done. 
    """
    pass


def download_tweets(handle):

    if sql.read_tl(handle.lower()) is not None:
        return(sql.read_tl(handle.lower())[2])
    else:
        # load vars for twitter api
        APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
        dotenv_path = os.path.join(APP_ROOT, '.env')
        load_dotenv(dotenv_path)

        tuo = TwitterUserOrder(handle)  # create a TwitterUserOrder

        # it's about time to create TwitterSearch object again
        ts = TwitterSearch(
            consumer_key=os.getenv("consumer_key"),
            consumer_secret=os.getenv("consumer_secret"),
            access_token=os.getenv("access_token"),
            access_token_secret=os.getenv("access_token_secret")
        )
        try:
            # start asking Twitter about the timeline
            tweets = [tweet["text"]
                      for tweet in ts.search_tweets_iterable(tuo)]

            text = ""
            for tweet in tweets:
                if tweet[0:2] != "RT":
                    text = text + \
                        re.sub(
                            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|\x00', '', tweet) + "."
            
            sql.write_tl(handle, text)
            return text
        except(TwitterSearchException):
            return "The selected user doesn´t have a valid timeline"
