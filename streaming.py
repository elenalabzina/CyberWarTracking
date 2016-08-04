from slistener import SListener
import time, tweepy, sys
from tweepy import OAuthHandler
import author
import sys
import time
import datetime

account = 2
authKit = author.Author(account)


def stream():
    #track = ['#targets', '#iceisis', '#opiceisis']
    account = 4
    authKit = author.Author(account)
    track = ['Targeted IS accounts']
    follow = ['3012875395','3012814332','82415925','3425725672','4720033461','3428485468','3063852029','3066135370']
    reload(sys)
    sys.setdefaultencoding('utf-8')
    name= datetime.datetime.strftime(datetime.datetime.now(), 'luckytroll%Y.%m.%d.%H.%M.%S')
    listen = SListener(authKit.api,"reports/"+name)
    stream = tweepy.Stream(authKit.auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track, follow=follow)
    except:
        print "error!"
        stream.disconnect()  


def main():
    #track = ['#targets', '#iceisis', '#opiceisis']
    track = ['Targeted IS accounts']
    follow = ['3012875395','3012814332','82415925','3425725672','4720033461','3428485468','3063852029','3066135370']
    reload(sys)
    sys.setdefaultencoding('utf-8')
    name= datetime.datetime.strftime(datetime.datetime.now(), 'luckytroll%Y.%m.%d.%H.%M.%S')
    listen = SListener(authKit.api,"reports/"+name)
    stream = tweepy.Stream(authKit.auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track, follow=follow)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()