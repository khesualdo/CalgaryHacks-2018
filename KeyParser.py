import configparser
from icecream import ic

config = configparser.ConfigParser()
config.read('TwitterKeys.ini')
config.sections()

consumer_key = None
consumer_secret = None
access_token = None
access_token_secret = None

if 'CONSUMER' in config:
    consumer_key = config['CONSUMER']['consumer_key']
    consumer_secret = config['CONSUMER']['consumer_secret']

if 'ACCESS' in config:
    access_token = config['ACCESS']['access_token']
    access_token_secret = config['ACCESS']['access_token_secret']

ic(consumer_key)
ic(consumer_secret)
ic(access_token)
ic(access_token_secret)
