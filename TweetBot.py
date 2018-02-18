import tweepy
import KeyParser
from icecream import ic

from io import BytesIO
from PIL import Image
from urllib import request

def id(str):
    return '@'+str

def tag(str):
    return '#'+str

def getMap(geo_lat, geo_long):
    url = "http://maps.googleapis.com/maps/api/staticmap?center="+str(geo_lat)+\
    ","+str(geo_long)+"&size=800x800&markers=color:red%7Clabel:HAVANA%7C"+str(geo_lat)+\
    ","+str(geo_long)+"&zoom=14&sensor=false"

    buffer = BytesIO(request.urlopen(url).read())
    Image.open(buffer).save(str(abs(geo_lat))+'.gif','GIF')

    return str(abs(geo_lat))+'.gif'

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def tweet(tweet=None, geo_lat=None, geo_long=None):

    cfg = { 
        "consumer_key"        : KeyParser.consumer_key,
        "consumer_secret"     : KeyParser.consumer_secret,
        "access_token"        : KeyParser.access_token,
        "access_token_secret" : KeyParser.access_token_secret 
    }
    api = get_api(cfg)

    if tweet is None:
        raise Exception('No msg for tweet!')

    if geo_lat is not None and not isinstance(geo_lat, float):
        if not isinstance(geo_lat, int):
            raise Exception('Latitude should be a float or int')

    if geo_long is not None and not isinstance(geo_long, float):
        if not isinstance(geo_long, int):
            raise Exception('Longitude should be a float or int')

    try:
        gif = getMap(geo_lat, geo_long)
        status = api.update_with_media(filename=gif, status=tweet,lat=geo_lat,long=geo_long)
        # ic(status)
    except:
        ic("Error querying GoogleMaps")
        status = api.update_status(status=tweet)
        # ic(status)

tweet("asdd", 1.0, 5.0)