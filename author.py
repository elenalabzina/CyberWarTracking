import tweepy
from tweepy import OAuthHandler

class Author():
 

 		
    def __init__(self, account = 1):
       ....
        self.auth = OAuthHandler(self.consumer_key,self.consumer_secret)
        self.auth.set_access_token(self.access_token,self.access_secret)
        self.api      = tweepy.API(self.auth)
        
    

        
        
    
    
