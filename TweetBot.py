# Imports for sending tweets
import tweepy
import KeyParser

# Imports for Google Static Maps API
from io import BytesIO
from PIL import Image
from urllib import request

# Debug library
from icecream import ic

def id(str=None):
    if str is None:
        return None
    else:
        return '@'+str

def hash(str=None):
    if str is None:
        return None
    else:
        return '#'+str

'''
Uses Google Static Maps API to create a screenshot of
a centered map with a red marker at target locations

Name of the file created is MAP.gif, the name is constant,
since we do not need to save the screenshot for every tweet created.

Returns the name of the file created.
'''
def getMap(geo_lat, geo_long):
    url = "http://maps.googleapis.com/maps/api/staticmap?center="+str(geo_lat)+\
    ","+str(geo_long)+"&size=800x800&markers=color:red%7Clabel:HAVANA%7C"+str(geo_lat)+\
    ","+str(geo_long)+"&zoom=14&sensor=false"

    # BytesIO creates in-memory file object
    # buffer can be used as input or output to most 
    # functions that expect a standard file object.
    buffer = BytesIO(request.urlopen(url).read())

    # Open the image from buffer (simulates a file)
    # Save the buffer as a GIF (create the map image)
    Image.open(buffer).save('MAP.gif','GIF')
    return 'MAP.gif'

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

    # Accept lat as float or int
    if geo_lat is not None and not isinstance(geo_lat, float):
        if not isinstance(geo_lat, int):
            raise Exception('Latitude should be a float or int')

    # Accept long as float or int
    if geo_long is not None and not isinstance(geo_long, float):
        if not isinstance(geo_long, int):
            raise Exception('Longitude should be a float or int')

    try:

        # Send a tweet with map, lat, long
        gif = getMap(geo_lat, geo_long)
        status = api.update_with_media(filename=gif, status=tweet,lat=geo_lat,long=geo_long)
    except:
        ic("Error querying GoogleMaps")

        # Send a tweet with lat, long
        status = api.update_status(status=tweet)