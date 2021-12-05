import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

##  Any functions can go here   ##


def main():
    api = create_api()
    while True:
        ##The function goes on this line
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()