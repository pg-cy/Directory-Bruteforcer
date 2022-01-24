#File integrity checker--run this script in a newly created folder you have permissions-->it will create 2 additional files for processing data
# When executing this script, you must be in the same folder as the script and the 2 additional files created.
import os
import hashlib
import sys

  

#hashing files
def hashes (f):
    file_sha256=hashlib.sha256()
    BLOCK_SIZE=65536
    fb=f.read(BLOCK_SIZE)   #reads file in chuncks stores it in fb
    while len(fb)>0:
        file_sha256.update(fb)  #keeps reading each block_size and updates with new hash until finished reading
        fb=f.read(BLOCK_SIZE)
    return file_sha256.hexdigest()  #displays hash value in hexadecimal

if len(sys.argv)==2 or len(sys.argv)>2:
    if sys.argv[1]=="check":
        try:
            watchlist=open("watch_list.txt", 'r')
            watchlist=watchlist.read().splitlines()
            hashlist=open("hash_list.txt",'r')
            hashlist=hashlist.read().splitlines()
            i=0
            for path in watchlist: 
                f=open(path,'rb')
                hw=hashes(f)
                f.close()  
                if hw!=hashlist[i]:
                    print(path+"      File changed--Hashes do not match!")
                i+=1

            print("------------------------------------------------")
            print("check completed")
            exit()
        except FileNotFoundError:
            print("\\\\Syntax error: cant use 'check' argument yet//")
            print("--Watch_list.txt/hash_list.txt not found!--")
            exit()
    elif sys.argv [1]=="new":
            os.remove("watch_list.txt")
            os.remove("hash_list.txt")
    else:
        pass      

# #keep asking for files to monitor--stores it in a list
print ("Add files to montior:                                      python3 file_monitor.py")
print("Check files to see if they have been modified:             python3 file_monitor.py  check")
print("Delete all previous monitored files and start over:        python3 file_monitor.py  new ")
print("--------------------------------------------------------------------------------------")
files_list=[]
file_name=input("Enter absolute path (full path) to files you want monitored\n")
while file_name!='done' and file_name!='Done':
    files_list.append(file_name)
    file_name=input()

print ()            
print("----Files Monitored--------------------")
notexist=[]
exists=[]
#Create the watch/hash list files to store data
f=open("watch_list.txt",'a')
f.close()
f=open("hash_list.txt",'a')
f.close()
for L in files_list:
    if os.path.isfile(L)==True:
        print(L)
        exists.append(L)
        f=open("watch_list.txt",'a')    #store the file paths that do exist in a watch_list.txt file
        f.write(L+"\n")
        f.close()
    else:
        notexist.append(L)
print("-----Files not found!-------")        
for nf in notexist:
    print(nf)

#-----------------------------------------------------------------------------
#hashing the files into hashes.txt file
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Hashing files now~~beep boop~~~~")
watchlist=open("watch_list.txt", "r")
watchlist=watchlist.read().splitlines()     #get rid if '\n' in each line

#hashes each file path in watch_list.txt
for path in exists: 
    f=open(path,'rb')
    hashed=hashes(f)    #hashes each path in 'exists' list
    f.close()  
    hf=open("hash_list.txt",'a')
    hf.write(hashed+"\n")   #write hashes to hash_list.txt file
    hf.close()
    print(hashed,end='   ')  
    print(path)

os.chmod("watch_list.txt",0o600) #reduce file permissions to increase security
