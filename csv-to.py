'''
Author: Anveshak Singh @singhanveshak
Date: 18,11,2023
This script will take your CSV file and 
    1) parse it json file
    2) indent it beautifully
USAGE: $> python csv-to.py file.csv
'''

import sys
filename=sys.argv[1]

with open(filename) as f:
    cols=f.readline().strip().split(sep=',')            #name of cols
    line1=f.readline()                          #reading first line too

def indent_to_txt(filename: str):
    '''indents file beautifully'''
    newname=filename.split('.')[0]+'.txt'
    ret=open(f'{newname}','w')             #set up
    width_cols=[]                                   #calculating appropriate size of cols
    for i in range(len(cols)):
        if( len(cols[i]) > len(line1[i])):
            width_cols.append(len(cols[i])+4)
        else:
            width_cols.append(len(line1[i])+4)
                                                    #start writin to copy file
    with open(filename) as f:
        line=""
        while(line!=['']):
            line=f.readline().strip().split(',')
            i=0
            x=""
            for ele in line:
                x+=ele+" "*(width_cols[i]-len(ele))
                i+=1
            ret.write(x+"\n")
    ret.close()
    print(f'formatting success... file written to {newname}')

def to_json(filename: str):
    '''parse to json'''
    newname=filename.split('.')[0]+'.json'
    ret=open(f'{newname}','w')             #set up
    n_cols=len(cols)

    with open(filename) as f:                      #start writing to copy file
        line=f.readline()
        ret.write("[\n")
        while(line!=['']):
            line=f.readline().strip().split(',')
            print(f"for {line}")

            i=0
            x=""
            for col,ele in zip(cols,line):
                x+=f'"{col}":"{ele}"'
                if(i!=n_cols-1):
                    x+=',\n'
                else:
                    x+='\n'
                i+=1

            ret.write('{\n'+x+'},\n\n')
        ret.write("]")

    ret.close()
    print(f'formatting success... file written to {newname}')

try:
    c=int(input(('You want ot export to\n1)json or 2)txt ?\n')))
    if(c==2):
        indent_to_txt(filename)
    elif(c==1):
        to_json(filename)
    else:
        print("Wrong choice :(")    
except Exception as e:
    print(f'Formatting failed\nError raised: {e}')
    