#purpose of script = helper to Mobile_Recharge.sh script
#author = Anveshak Singh
#date = Fri Dec 15, 2023
#contact = anveshaksingh123@gmail.com

import orjson
import pandas as pd
import sys

file_path = sys.argv[1]
_sms = sys.argv[2]
_talk = sys.argv[3]
_data = sys.argv[4]

with open(file_path, 'r') as file:
    json_string = file.read()
dic = orjson.loads(json_string)

print("==================================================================================")
print("Plans are sorted in descending order of Value-to-Cost")
print("==================================================================================")

glist=dic['groupings']

for Type in glist:                    #for each group in glist. Each "Type" is a dictionary
  
  name=Type['name']
  productList=Type['productList']     #each productList is a list
  lst=[]                              #create an empty list

  for plan in productList:            #each plan is a dictionary
    data=plan['data']
    sms=plan['sms']
    producttype=plan['producttype']
    validity=plan['validity']
    description=plan['description'].replace(' ','_')
    price=int(plan['price'])
    
    #GETTING ALL DATA TO PUT INTO GOODNESS FORMULA
    if(validity=='NA'):
      n_validity=1
    else:
      n_validity=int(validity.split()[0])

    if(sms=='NA'):
      n_sms=1
    else:
      n_sms=int(sms.split()[0])

    if("U/L" in description or "Unlimited" in description or "unlimited" in description):
      talk=101
    else:
      talk=1
    
    if(data=='NA'):
      n_data=1
    elif('Day' in data):
      n_data=float(data.split()[0])*n_validity
    else:
      n_data=float(data.split()[0])

  #CALCULATING GOODNESS AND CHECKING CONDITION FOR PRINTING
          
    if(_data=='1' and _talk=='1' and _sms=='1'):
      condition= n_data!=1 and talk==101 and n_sms!=1
      goodness=n_sms*n_data*n_validity/price
    elif(_data=='1' and _talk=='1' and _sms=='0'):
      condition= n_data!=1 and talk==101
      goodness=n_data*n_validity/price + n_sms
    elif(_data=='1' and _talk=='0' and _sms=='1'):
      condition= n_data!=1 and n_sms!=1
      goodness=n_sms*n_data*n_validity/price 
    elif(_data=='0' and _talk=='1' and _sms=='1'):
      condition= talk==101 and n_sms!=1
      goodness=n_sms*n_validity/price + n_data
    elif(_data=='0' and _talk=='0' and _sms=='1'):
      condition= n_sms!=1
      goodness=n_sms*n_validity/price + n_data
    elif(_data=='0' and _talk=='1' and _sms=='0'):
      condition= talk==101
      goodness=n_validity/price + n_sms + n_data
    elif(_data=='1' and _talk=='0' and _sms=='0'):
      condition= n_data!=1
      goodness=n_data*n_validity/price + n_sms
    else: 
      condition=True
      goodness=n_sms*n_data*n_validity/price
    
    # print(f"before checking, sms={sms},talk={talk},data={data},validity={validity},condition={condition},type(goodness)={type(goodness)},goodness={goodness},type={producttype=='Recharge'}")
    if(condition and producttype=='Recharge'):
      lst.append([goodness,data,sms,validity,price,description])
  
  df=pd.DataFrame(lst,columns=['Goodness','Data','SMS','Validity','Price(₹)','Talktime/Description'])
  df.sort_values(by=['Goodness'],ascending=False)
  print('\n\n================================[ '+name+' ]================================\n\n')
  if(not df.empty):
    print(df[['Data','SMS','Validity','Price(₹)','Talktime/Description']])
print("==================================================================================")

