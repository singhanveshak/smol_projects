import sys
import subprocess
import re

url = sys.argv[1]
DEPTH = 0
MAXDEPTH = 2
VISITED_URLS_HASH = []	#stores hashes of visited urls
VISITED_URLS = []
VISITED_MAILS = []
VISITED_MAILS_HASH = []	#stores hashes of mails

def hash(string: str) -> int:
    hash_value = 5381
    for char in string:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value

def collect_new_mails(line: str):
	email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	emails_found = re.findall(email_pattern, line)
    
	for mail in emails_found:
		if(hash(mail) not in VISITED_MAILS_HASH):
			VISITED_MAILS.append(mail)
			VISITED_MAILS_HASH.append(hash(mail))

def collect_new_urls(line: str)->list:

	global MAXDEPTH
	global DEPTH	
	urls_found = []
	if(DEPTH<=MAXDEPTH):
		# url_pattern = r'<a\s+(?:[^>]*?\s+)?href="(https?://(?:www\.)?vnit\.ac\.in/[^"]*)"'
		url_pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
		urls_found = re.findall(url_pattern, line)

		new_urls=[]
		for url in urls_found:
			if(hash(url) not in VISITED_URLS_HASH):
				VISITED_URLS_HASH.append(hash(url))
				VISITED_URLS.append(url)
				new_urls.append(url)
	return new_urls

def visit(url: str):

	global MAXDEPTH
	global DEPTH

	command = f'curl {url}'
	result = subprocess.run(command, shell=True, capture_output=True, text=True)
	output = result.stdout.splitlines()
	print('VISTING','AT DEPTH',DEPTH,url)
	
	#collect new urls and mails
	new_urls=[]
	for line in output:
		collect_new_mails(line)			
		new_urls.extend(collect_new_urls(line))
	# print('NEW URLS FOUND',new_urls)
	
	#visit new_urls
	for url in new_urls:
		if(DEPTH<MAXDEPTH):				
			DEPTH+=1
			visit(url)
			DEPTH-=1
			
try:
	visit(url)

except:
	print("ERROR")
	print(VISITED_MAILS)

finally:
	print("FOLLOWING MAILS COLLECTED THUS FAR:\n")
	for i in VISITED_MAILS:
		print(i)