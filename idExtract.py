'''
Created on Mar 7, 2016

@author: lenchick
'''
import glob,os
import idExtractor
import random


def idExtact():
    data_dir = 'reports/'
    base= 'id_stack/'
    names = os.path.join(data_dir, '*.json')
    files = glob.glob(names)
    date=""
    rand =  random.randint(1,100)

    for file in files:
        print(file)
        index = file.find("2016")
        new_date = file[(index+5):(index+10)]
        if (new_date!=date):
           date=new_date
        file1 = os.path.join(base,date+"_"+str(rand)+"_users.csv")
        file2 = os.path.join(base,date+"_"+str(rand)+"_rid.csv")
        idExtractor.extractIDs(file, file1, file2)
        ff = 'oldreports'+"/"+file.split('/')[1]
        os.rename(file,ff)
