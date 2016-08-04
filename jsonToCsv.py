import json
from django.utils.encoding import smart_str, smart_unicode

def jsonCSV(source="out\\03.05Out.csv", target = "out\\final\\03.05OutFINAL.csv", first=True):
    source_file = open(source,'rb')
    if (first):
        output_file = open(target,'w')
    else:
	output_file = open(target,'a')
    l = source_file.readline()

    flag=True
    while (l!=''):
        user = json.loads(l, encoding='utf-8',)
        user=eval(user)
    
        if (flag and first):
            for key in user.keys():
                if (key=="description"):
                    continue
                output_file.write(str(key))
                output_file.write("^") 
            flag = False
            output_file.write('description\n')
    
        for key in user.keys():
            
            out = smart_str(user[key])
            if (key=="description"):
                decription=out.replace("\t","...")
                decription=decription.replace("\n"," | ")
                decription=decription.replace("\u0085"," | ")
                continue
            if (key=="location"):
                out = out.replace("\t","...")
            output_file.write(out)
            output_file.write("^") 
                
    
        output_file.write(decription)
        output_file.write("\n")        
        l = source_file.readline()

    
    output_file.close()
    


    source_file.close() 
    
#jsonCSV()