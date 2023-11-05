'''
This script will allow you to set and track progress, for:
    1. challanges (CH)
    2. projects    (PR)
    3. daily reminders to you   (RE)
For example a new workout challange: 50 pushups/day; it makes sure you do that; reminds you why you started it in the first place

TODO: 
1.     build a database of past and current CHs, PRs, REs: records dates and numeric parameters, generates a graph or progress bar if you want (file handling)
2.     then provide an interface of interaction: gives last progress report, date, time; then asks for progress since last recorded; gets it, records it
3.     If progress is not healthy; it asks you to lower the bar
4.     mails you reports every 2 days

DATABASE: give a unique ID to each CH, PR, RE
double asterisk** seperated values: ID**name_of_challange**reason_for_beginning_challange**name_of_progress_parameter**date:newprogress**date:newprogress**...
Regarding ID: it will be a no. like xyz 122; first digit:0(for done)/1(for active),second_digit for CH,PR,RE : 0,1,2, third_digit category:1cybersec/2sports/3drawing/4
'''
from datetime import date
import matplotlib.pyplot as plt

filename='db.txt'
categ=['cybersec','sports','art']
choice=1
id=000
dash='-----------------------------------------------------------------------------------------------------'
# with open(filename,'r') as f:
#     for line in f.readlines():
#         l=line.strip().split('**')
def add_record():
    x=1
    y=input('What?\tshort challange (1)\tnew project (2)\t reminder (3) ')
    z=input('which category: cybersec (1)\tsports (2)\tdrawing (3) ')
    name=input('what name would you give to your challange? ')
    why=input('why do you want to start this project/challange? ')
    param=input('name of progress parameter? For example no. of drawings done/pushups done. Advice: Enter numeric param(or the plot function crashes)!!  ')
    progress=input(f'ok for date {date.today()} enter progress...')
    with open(filename,'a') as f:
        print(f'Adding to new record:\t\t{x}{y}{z}**{name}**{why}**{param}**{date.today()}:{progress}')
        f.write(f'\n{x}{y}{z}**{name}**{why}**{param}**{date.today()}:{progress}')
    
def add_progressto(id):
    with open(filename,'a+') as f:
        f.seek(0)
        for l in f.readlines():
            if(l[:3]==id):
                progress=input(f'ok for date {date.today()} enter progress...')
                f.write(f"**{date.today()}:{progress}")
                return
    print(f'ID {id} not found !')

def deactivate_record(id):
    found=0
    with open(filename) as f:
        data=f.readlines()
    for i in range(len(data)):
        if(data[i][:3]==id):
            data[i]=f'0{data[i][1:]}'
            found=1
        if(found==0):
            print(f'ID {id} not found !')
            return
    with open(filename,'w') as f:
        f.writelines(data)

def graph(id):
    x=''
    with open(filename) as f:
        for l in f.readlines():
            if(l[:3]==id):
                x=l
                break
    if(x==''):
        print(f'ID {id} not found !')
        return
    info=x.strip().split('**')
    dates=[]
    progress=[]
    for pair in info[4:]:
        print(pair)
        dates.append(pair.split(':')[0])
        progress.append(int(pair.split(':')[1]))
    print(dates,progress)
    plt.plot(dates,progress)
    plt.title(f"Progress for challange {info[1]}")
    plt.show()

print('here\'s all the summary of your challanges')

choice=int(input(f'{dash}\nadd_progressto (1)\ndeactivate_record (2)\ngraph (3)\nadd_record (4)\nEnter 0 to exit\n{dash}'))
while(choice!=0):
    if(choice==1):
        id=input('Enter ID of the record to add progress to ')
        add_progressto(id)
    elif(choice==2):
        id=input('Enter ID of the record to deactivate ')
        deactivate_record(id)
    elif(choice==3):
        id=input('Enter ID of the record to graph ')
        graph(id)
    elif(choice==4):
        add_record()
    else:
        print('bad choice! Try Again')
    choice=int(input(f'{dash}\nenter choice again '))
