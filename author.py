import tweepy
from tweepy import OAuthHandler

class Author():
 

 		
    def __init__(self, account = 1):
        if (account==1):
            self.consumer_key = 'ScJOL6C7lZFiY1iJCd8GhF0ZO'
            self.consumer_secret = 'sIWnlAlZCVa7MoqUIi070hd3yE2WpJePnjyXZ9ZruSkY2WzRsw'
            self.access_token = '4849805748-K6W5Fi41hZHoav8ru4caZc5kYsUnuVEo0llitvZ'
            self.access_secret = 'OfKFjHqrwwSYlN2hlNG7Y28y7UuKwlIIKDw1TL8xyDWE3'
            self.account = 1
        if (account==2):
            self.consumer_key = 'DYtIQLPpr8k7ozWNj1jsPilQ2'
            self.consumer_secret = 'c21zXW9jjx0yOg6pXprmZGz0hpxpwMQlz6tbs0K5ibvaRXrXFD'
            self.access_token = '4875483255-7a289bMhknlLtjSqPKZ8Jcy8KSeIhojHeIw2AaK'
            self.access_secret = 'CYrpBgkVbH7RbjIA2WJzQdR0xnr1PKvELhdXkMXjr5uy0'
            self.account = 2
        if (account==3):
            self.consumer_key = 'ewZVcWqmpK0Nn9DjuYYRKSzNU'
            self.consumer_secret = 'ARHcRhqE83ZRpAgxLwH9x5gVfzQtyvzvu2xPFGJGj4NSUk1xbg'
            self.access_token = '4818138955-177mgVFXAWxjVxZEu0s41AG8YvUkUR3lCRnJXVa'
            self.access_secret = 'GXGfRfc3ZPhurHitYBMd3wZxNxZ9CLl0KsZJb4mxwJTd5'
            self.account = 3
        if (account==4):
            self.consumer_key = 'v9zcsA5IHlAvqpCo8daXkrIoB'
            self.consumer_secret = 'OVarwAFilYcCONyU4DcfdWkTgrAlx7bHGc4Mul9wU1xd77RBXq'
            self.access_token = '4885756394-2pzaqXUdwfqRnSwbSEykwMTzN6JbYwAa3nwHSrY'
            self.access_secret = 'aZPOc5peAWZWgCXWsByLYLZoDoqXgB6imF2kjv5YAeLsR'
            self.account=4
#work1@lenchick.net
        if (account==5):
            self.consumer_key = 'vLhhtxkgpF2qohATWuy2vz9b2'
            self.consumer_secret = 'IzD3pGr7F3QRISXqeI5BsoGD4cBYCvwasMuNU4CIghSjXXRd70'
            self.access_token = '725147558335619072-HE5YRiFA2zRZrghMP8GAsZb33el7y8T'
            self.access_secret = 'qDzsARc4XA45lzOdHqpqr7Q4nPgQvE5qayK8LUhh91BCr'
            self.account=5
#work2@lenchick.net
	if (account==6):
            self.consumer_key = 'HElc1KF3WrxOoiERiDvgfEDYV'
            self.consumer_secret = 'CKNc8YZP0slvGmB3Tsh16sOiSPrBpoJGMxmzV6YClSltKpWZdv'
            self.access_token = '725149572666933250-LZ2UGETr1DKRRXaNHXzeazyoUwvbiY2'
            self.access_secret = 'FLVuJtH1k1omN2yIK2fCneH8Bh2zyTEzdW35g5P9banss'
            self.account=6
#work3@lenchick.net
	if (account==7):
            self.consumer_key = 'sS2NWfcSdC1CDWJL63OLPRqID'
            self.consumer_secret = 'umvQCWt0MknpCMsxTpRVgbxH3uEk6nJgH3YsS33gFZvOWeHTf4'
            self.access_token = '725157767007358982-c2iupdAaa03whtacIFHVVpucXyargeV'
            self.access_secret = '06mPIsU8a6vKvbfCRiYbzOayuVTR1XGGaIQEaNGhAIE6b'
            self.account=7
#work4@lenchick.net
	if (account==8):
            self.consumer_key = 'DDCyO0hgFXE6QZeTtX0cWEfFi'
            self.consumer_secret = 'ojWWiesFcOf99qzjEvTQXJ8c6h7rsMB1Vc0cbFFLg2fiJOF0IX'
            self.access_token = '725158852409319424-yYIVuezKeQQzMZWYBI6KWim2K5b3Ocd'
            self.access_secret = 'mhcYoRcBR4DvrK1P5Etd7HOV2XwqIfeSv3X4WqJEcabwW'
            self.account=8
#work5@lenchick.net
	if (account==9):
            self.consumer_key = 'eSCbvdCF0oKFoh89Sq8tagiMX'
            self.consumer_secret = 'l8Ug1l7b8bdl5x6xBB2kViemnnGziEQLAocSb4XEl9VqWaSeip'
            self.access_token = '725159569677234176-HVQRQThShbwUZxGDHbFJpyj5EVoVhwc'
            self.access_secret = 'N3haKO86SU4kekOnfYjJat8BzNROD4sZOVNwIovD9jHdN'
            self.account=9
#work6@lenchick.net
	if (account==10):
            self.consumer_key = 'IdKon5HBUjAkB7hExDyA1Idcg'
            self.consumer_secret = 'U9yuPcShnHihEuMHa4Ol9MdAJyAh5gwZVqqHIHJD1f0xT3ngx2'
            self.access_token = '725160917760118785-LHoVSYkDKB1rpZmmGIhfVnK7kX6fPmG'
            self.access_secret = '9ghG6fpKEFcpvVNA1e6RsiDBKT4tERiod9MLNxPFWlVr2'
            self.account=10
        self.auth = OAuthHandler(self.consumer_key,self.consumer_secret)
        self.auth.set_access_token(self.access_token,self.access_secret)
        self.api      = tweepy.API(self.auth)
        
    

        
        
    
    