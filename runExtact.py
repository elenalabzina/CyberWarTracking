import schedule
import time
import processRep
from time import gmtime, strftime
import mail

#schedule.every().day.at("19:25").do(processRep.doRun,'It is 18:19')

while True:
    #schedule.run_pending()
    print("It is time to run the script!")
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    processRep.doRun()
    print("Done for today!")
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    mail.mail()
    time.sleep(60*60*24) # wait one day
