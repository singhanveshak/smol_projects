'''
This script formats/beautifies code written in different languages.
CURRENTLY SUPPORTING: C, C++,C#, java, BASH
ALGORITHM CHOICE: Go to every character 1 by 1-> collect lines (break them at ; } {  '')-> write to file
EXAMPLE FILE: temp.js
USAGE: $>python code-formatter.py temp.c
'''
import sys
file_name=sys.argv[1]

def check_script(file_name: str) -> int:
    '''Checks the programming language of a file'''
    ext=file_name.split(".")[-1]    #extension of the file
    if(ext=='cpp' or ext=='c' or ext=='cs' or ext=='java' or ext=='js'):    
        return 0
    elif(ext=='sh'):
        return 1
    elif(ext=='py'):
        return 2
    else:
        return -1

def format_c(filename):
    '''foarmat C, C++, csharp, java code'''

    copy=open(f'formatted_{filename}','w')
    count=0     #THIS VAR KEEPS TRACK OF NUMBER OF OPENED BRACKETS


    with open(filename) as f:
        ch=' '
        while(ch!=''): 

            #COLLECT LINES FROM FILE
            line=''
            ch=' '
            while(ch!=';' and ch!='}' and ch!='{' and ch!=''):
                ch=f.read(1)          
                line+=ch
            #WRITE THE LINE
            if(ch=='}'):
                count-=1 
            if(count<0):
                count=0
            if(ch=='{'):
                copy.write("\t"*count+line.strip()+"\n")                
                count+=1
            else:
                copy.write("\t"*count+line.strip()+"\n")


    copy.close()

def format_bash(filename :str):
    '''format bash code'''
    copy=open(f'formatted_{filename}','w')
    count=0     #THIS VAR KEEPS TRACK OF NUMBER OF OPENED BRACKETS
    with open(filename) as f:
        ch=' '
        while(ch!=''): 
            #COLLECT LINES FROM FILE
            line=''
            ch=' '
            while(ch!=';' and ch!='}' and ch!='{' and ch!=''):
                ch=f.read(1)          
                line+=ch
            #WRITE THE LINE
            if(ch=='}'):
                count-=1 
            if(count<0):
                count=0
            if(ch=='{'):
                copy.write("\t"*count+line.strip()+"\n")                
                count+=1
            else:
                copy.write("\t"*count+line.strip()+"\n")

try:
    if(check_script(file_name)==0):
        #if C, C++, csharp
        format_c(file_name)
        print(f'\nFormatting success...wriiten to formatted_{file_name}')
    
    elif(check_script(file_name)==1):
        #if bash
        print(f'\nFormatting success...wriiten to formatted_{file_name}')

    else:
        print("Formatting failed\nException raised:\tUnsupported file :(")

except Exception as e:
    print(f"Formatting failed\nException raised:\t{e}")    
