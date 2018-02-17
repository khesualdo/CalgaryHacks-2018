import tweepy
import KeyParser

def tag(str):
    return '@'+str

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
    tweet = "Hello, world!"
    status = api.update_status(status=tweet) 

if __name__ == "__main__":
  main()