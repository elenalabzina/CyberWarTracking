'''
Created on Feb 29, 2016

@author: lenchick
'''
import json
import sys
from sets import Set
import time

def monthToNum(date):

    return{
       	'Jan' : 1,
        'Feb' : 2,
        'Mar' : 3,
        'Apr' : 4,
        'May' : 5,
        'Jun' : 6,
        'Jul' : 7,
        'Aug' : 8,
        'Sep' : 9, 
        'Oct' : 10,
        'Nov' : 11,
        'Dec' : 12
	}[date]


def loadSet(spisok):
    f = open(spisok,'a')
    f.close()
    f = open(spisok,'r')
    a = Set()
    l = f.readline()
    
    while (l!=''):
        items = l.split('\n')
        a.add(items[0])
        l= f.readline()
    return a

def extractIDs(name='reports/luckytroll2016.03.15.20.54.46.json', outfile='test.csv', idfile="test2.csv"):
 
    to = open(outfile,'a')
    a=1
    count=0
    idis = loadSet(idfile)

    while (a==1):  
        a=2
        jR =   open(name, 'r') 
        l=jR.readline()

        while (l!=''):
            if (l=='\n'):
                l = jR.readline()
                continue        
            try:
                tweet = json.loads(l)
                created = tweet['created_at']
                dates = created.split()
                day = dates[2]
                month = monthToNum(dates[1])
                year = dates[5]
                cdate = day + "." + unicode(month) + "." + year
                urls = tweet['entities']['urls']
		bot = tweet['user']['screen_name'].encode('utf-8')
                time_zone = tweet['user']['time_zone'].encode('utf-8')
		try:
		     location = tweet['user']['location'].encode('utf-8')
                except:
		     location = "formaterror"					

       
                for url in urls:
                                              
                    str = url['expanded_url']
                    #print(str)   
                    #print('\n') 
                    #raw_input('')
                    str1 = "="
                    i = str.find(str1)
                    #raw_input(i)
                    #id = int(str[i+1:])
                    ids = str[i+1:]
                    try:
                        id = int(ids)
                    except:
                        continue
                    if ids in idis:
                        continue
                    idis.add(ids)
                    f= open(idfile,"a")
                    f.write(ids)
                    f.write('\n')
                    f.close()
                    
                    #print(id)
                
                    to.write(created)
                    to.write(',')  
                    to.write(cdate)
                    to.write(',')              
                    to.write(ids)
		    to.write(',')
		    to.write(bot)
		    to.write(',')
	            to.write(time_zone)		
                    to.write('\n')
          
      
            except:
                e = sys.exc_info()[0]
                print( "<p>Error: %s</p>" % e )
            
           
          
            l = jR.readline()
        to.close()
        
#extractIDs()