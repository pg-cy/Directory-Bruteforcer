def check_P(password):
#checking length
	if len(password)<8:
		print(u"\N{cross mark}| "+ "Pass not long enough!!!(8-characters)")
	else:
		print(u"\N{heavy check mark}| "+"pass length acceptable")	
	#-----------checking caps and special character--------------------------------------------
	x=0
	y=0
	for letter in password:	
		if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":			
			x+=1			
		if letter in "!@#$%^&*()":
			y+=1
	if x>0 and y>0:
		print(u"\N{heavy check mark}| "+"There is a capital in your password")
		print(u"\N{heavy check mark}| "+"There is a special-character in your password")
	elif x>0:
		print(u"\N{heavy check mark}| "+"There is a capital in your password")
	elif y>0:
		print(u"\N{heavy check mark}| "+"There is a special-character in your password")

	if x==0 and y==0:
		print (u"\N{cross mark}| "+"NO CAPS!!!")
		print (u"\N{cross mark}| "+"No special character:   !@#$%^&*()")				
		#--------------------------------------------------------------------
	elif x==0:
		print(u"\N{cross mark}| "+"NO CAPS!!!")
	elif y==0:
		print (u"\N{cross mark}| "+"No special character:   !@#$%^&*()")


def check_list(passw):
#open file, then read all lines as one (as one list)...notice the 'readlines' plural. (ables us to get length(len) of list)
	l = open(wordlst, "r",encoding="latin1")
	length_list = len(l.readlines())
	l.close()
#reopen file to read each line separately, the "r" means 'read' (mode-type)
	f=open(wordlst,"r",encoding="latin-1")
	n=0	
	for x in range (length_list):
		line = f.readline().strip()  #remove all white spaces in each line .strip
		if passw==line:		#finding if password is in wordlist
			print (u"\N{cross mark}| "+"Not secure!---pass found in wordlist")
			n+=1
			f.close()
			break
	if n==0:
		print(u"\N{heavy check mark}| "+"Secure pass---not found in wordlist")

print ("\\\\\\\\\\\\\A password complexity checker, also compares it against a workdlist (like rockyou.txt)///////")
print("-----------------------------------------------------------------------------------------------------------------")
passw=input("~~~Please enter password: ")
wordlst=input("~~~Please enter wordlist path: ").strip()
#keep looping searching for new passwords until user wants to stop
x="y"
while x=="y":
	print("---------------------------------")
	check_P(passw)
	check_list(passw)
	print("---------------------------------")
	cont=input("Try another password (y/n):  ").strip()
	if cont=="n":
		break
	print("---------------------------------")
	passw=input("~~~Please enter password: ")