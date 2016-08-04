import accountExtactor
import glob,os
import jsonToCsv

def aE():

    data_dir = 'id_stack/'
    base= 'out/'
    names = os.path.join(data_dir, '*users.csv')
    outfull = os.path.join(base,"outfullIPIS.csv")
    files = glob.glob(names)
    date=""

    for file in files:
        print(file)
        key = file.split('/')[1]
        outfile = os.path.join(base,key+".json",)
        accountExtactor.getUsers(file, outfile, key)
        jsonToCsv.jsonCSV(outfile,outfile+".csv")
        jsonToCsv.jsonCSV(outfile,outfull, False)
        ff = 'oldid'+"/"+ key
        os.rename(file,ff)

  

