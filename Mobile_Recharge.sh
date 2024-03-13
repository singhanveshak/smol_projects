#!/bin/bash

#purpose of script = sort your recharge plans according to most value per cost
#author = Anveshak Singh
#date = Fri Dec 15, 2023
#contact = anveshaksingh123@gmail.com

echo -e "enter your operator\n"
echo -e "\tBSNL..(1)\tMTNL..(2)\tAirtel..(3)\tjio..(4)\tvi..(5)"
read  choice

file_name='plans'
if [ $choice -eq 1 ]; then
  curl 'https://digitalcatalog.paytm.com/dcat/v1/browseplans/mobile/7166?channel=web&version=2&child_site_id=1&site_id=1&locale=en-in&operator=BSNL&pageCount=1&itemsPerPage=20&sort_price=asce&pagination=1' \
  --compressed --silent  2>err_log | jq | cat > $file_name.json

elif [ $choice -eq 2 ]; then
  curl 'https://digitalcatalog.paytm.com/dcat/v1/browseplans/mobile/7166?channel=HTML5&version=2&child_site_id=1&site_id=1&locale=en-in&operator=MTNL&pageCount=1&itemsPerPage=20&sort_price=asce&pagination=1' \
  --compressed --silent  2>err_log | jq | cat > $file_name.json

elif [ $choice -eq 3 ]; then
  curl 'https://digitalcatalog.paytm.com/dcat/v1/browseplans/mobile/7166?channel=web&version=2&child_site_id=1&site_id=1&locale=en-in&operator=Airtel&pageCount=1&itemsPerPage=20&sort_price=asce&pagination=1' \
  --compressed --silent  2>err_log | jq | cat > $file_name.json

elif [ $choice -eq 4 ]; then
  curl 'https://digitalcatalog.paytm.com/dcat/v1/browseplans/mobile/7166?channel=HTML5&version=2&child_site_id=1&site_id=1&locale=en-in&operator=Vodafone%20Idea&pageCount=1&itemsPerPage=20&sort_price=asce&pagination=1&circle=Gujarat' \
  --compressed --silent  2>err_log| jq | cat > $file_name.json

elif [ $choice -eq 5 ]; then
  curl 'https://digitalcatalog.paytm.com/dcat/v1/browseplans/mobile/7166?channel=HTML5&version=2&child_site_id=1&site_id=1&locale=en-in&operator=Vodafone%20Idea&pageCount=1&itemsPerPage=20&sort_price=asce&pagination=1' \
  --compressed --silent  2>err_log| jq | cat > $file_name.json

else
  echo "Wrong choice! " 
fi

echo "If you enter all as don't care, we will sort all the best plans."

echo  "Do you want sms? yes..(1)	don't care..(0)"
read  sms

echo  "Do you want talktime? yes..(1)	don't care..(0)"
read  talktime
 
echo  "Do you want data? yes..(1)	don't care..(0)"
read  data

python3 please_process.py $file_name.json $sms $talktime $data 2>err_log

#rm plans.json 2>err_log

