import requests
import sys
#if sys args does not equal 2 exit
arg_len = len(sys.argv) -1 
if (arg_len!=2):
    print ("############|   syntax$$: python3 <script.py>   <url>   <wordlist>   |############")
    exit()
    

url = (sys.argv[1])
wordlist = (sys.argv[2])

print("--------------Web server response:-------")
resp = requests.get(url)
print (resp)
print (resp.status_code)
print("-----------------------------------------")

#the remN.rstrip() method removes the \n from each item in list 'f' 
#(if you were to just f.readlines() itll look like this  [pass\n] [password123\n] [prince44\n]
with open(wordlist) as f:
	#line = f.readlines()
	lines = [remN.rstrip() for remN in f]



for x in lines:
	new_url = (url+"/"+x)
	resp = requests.get(new_url, allow_redirects=False).status_code
	if (resp!=404):
		print (new_url+"               status: ("+ str(resp)+")")
	