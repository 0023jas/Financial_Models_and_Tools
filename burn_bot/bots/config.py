##imports
import tweepy
import logging
import os

##Returns a logger with a specified name
logger = logging.getLogger()

def create_api():
    '''
    This function reads the authentication creadentials
    from the environmental variables and creates the
    Tweepy API object.
    '''
    ##The following environment variables go here
    consumer_key = "API key goes here"
    consumer_secret = "API Key Secret goes here"
    access_token = "Access Token goes here"
    access_token_secret = "Access Token Secret goes here"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
