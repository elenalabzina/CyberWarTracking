import author
from datetime import datetime
import time
import tweepy
import json
import os
import urllib
#import jsonToCsv

def getUsers(catalogue="_rawtweets_3_1_users.csv", outfile="resultAccounts_full24.json",key=""):

    picaddress = key
    if not os.path.exists(picaddress):
        os.makedirs(picaddress)
    f = open(catalogue,"r")
    l = f.readline()
    print(l)
    authKit = author.Author(1)
    counter=0
    while (l!=''):
        items = l.split(',')
        created = items[0]
        created_short = items[1]  
        #created ="3\01\2016"
        id = items[2].split('\n')[0]
        bot = items[3]
        bot_timezone = items[4].split('\n')[0]

        print(id)
        try:
            id = int(id)
        except:
            print(id)
            print("Error - ID non-integer")
            l = f.readline()
            continue
        
        try:
            user = authKit.api.get_user(id)
            d= user.__dict__
            created_at = d['created_at']
            createdat=created_at.strftime("%c")
            createdat_short = created_at.strftime("%m.%Y")
            location = d['location'].encode('utf-8')
            description = d['description'].encode('utf-8')
            description = description.replace('^'," ")
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	    now_short  = datetime.now().strftime('%d.%m.%Y')	
            #desc =  description['description'].replace("\n", " | ")
            dic = {'time_now_chicago': now, 'time_now_chicago_short': now_short,'report_created': created,  'report_created_short': created_short, 'bot': bot, 'bot_timezone': bot_timezone,
	    'source_id': id, 'exists': True, 
            'has_extended_profile': d['has_extended_profile'], 'description': description , 'profile_use_background_image':d['profile_use_background_image'],
            'time_zone': d['time_zone'], 'verified': d['verified'], 'followers_count': d['followers_count'], 
            'geo_enabled': d['geo_enabled'], 'lang': d['lang'], 'statuses_count': d['statuses_count'],
            'friends_count': d['friends_count'], 'favourites_count': d['favourites_count'], 'account_created': createdat, 'account_created_short':createdat_short,
            'location': location, 'default_profile': d['default_profile'], 'profile_image_url': d['profile_image_url'], 'screen_name': d['screen_name']}
            ids = str(id)
            picname = os.path.join(picaddress,ids+".jpeg")
            address = d['profile_image_url']
            urllib.urlretrieve(address,picname)
            
        except tweepy.TweepError as e:
            try:
		print(e.message[0]['code'])
            
            	if (e.message[0]['code']==88):
                    if (authKit.account<3):
                         authKit=author.Author(authKit.account+1)
                         print("account:")
                         print(authKit.account)
                         continue
                    else:
                        print("Going to sleep")
                        time.sleep(10 * 60)
                        authKit=author.Author(1)
                        continue
            except:
		print("This is weird...But I am going on")
	    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            now_short  = datetime.now().strftime('%d.%m.%Y')
            dic = {'time_now_chicago': now, 'time_now_chicago_short': now_short, 'report_created': created,  'report_created_short': created_short, 'bot': bot, 'bot_timezone': bot_timezone,
            'source_id': id, 'exists': False, 
            'has_extended_profile': '', 'description': '','profile_use_background_image':'',
            'time_zone': '', 'verified': '', 'followers_count': '', 
            'geo_enabled': '', 'lang': '', 'statuses_count':'',
            'friends_count':'', 'favourites_count': '', 'account_created':'', 'account_created_short':'',
            'location': '','default_profile': '', 'profile_image_url': '', 'screen_name': ''}
        
 
        
        with open(outfile, "a") as ffile:
            counter=counter+1
            print(counter)
            json.dump(unicode(dic), ffile, encoding='utf-8')
            ffile.write("\n")
        l = f.readline()
        
    f.close()   

#print("hi")    
#getUsers()
#jsonToCsv.jsonCSV()
