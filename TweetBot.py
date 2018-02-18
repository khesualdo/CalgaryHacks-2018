import tweepy
import KeyParser

from io import BytesIO
from PIL import Image
from urllib import request

def tag(str):
    return '#'+str

def getMap(geo_lat, geo_long):
    url = "http://maps.googleapis.com/maps/api/staticmap?center="+str(geo_lat)+","+str(geo_long)+"&size=800x800&zoom=14&sensor=false"
    buffer = BytesIO(request.urlopen(url).read())
    Image.open(buffer).save(str(abs(geo_lat))+'.gif','GIF')

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():

    cfg = { 
        "consumer_key"        : KeyParser.consumer_key,
        "consumer_secret"     : KeyParser.consumer_secret,
        "access_token"        : KeyParser.access_token,
        "access_token_secret" : KeyParser.access_token_secret 
    }

    api = get_api(cfg)
    tweet = "Havana na na na"
    geo_lat = 1.3552217
    geo_long = 103.8231561
    gif = getMap(geo_lat, geo_long)
    # status = api.update_with_media(filename=gif, status=tweet,lat=geo_lat,long=geo_long)

if __name__ == "__main__":
    main()