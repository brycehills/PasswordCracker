import sys
import hashlib #library to implement md5
import binascii # for hex conversion

def encrypt(pw, salt, magic):
  
	#*******************************initialization******************************
	alt = pw + salt + pw        #get alt
	res = pw + magic + salt		#compute res
	print("res = " + res)
	
	h = hashlib.md5(alt.encode()).hexdigest()
	print("h= " + h)
	
	l = len(pw)	# get len(pw) -- should be 6 in our case
	print("l = " + str(l))
	
	while l > 0:
		res = res + h[0:min(16,l)]
		l = l - 16
		
	print("\nres after 1st while loop = " + res)
	print("in hex: " + str(res.encode().hex()))
	print("\n")
	
	l = len(pw) #reset l
	# For each bit in length(password), from low to high 
	while l:
		if l & 1:
			res += '\0' # append null chr
		else:
			res += pw[0:1] # append first bit of pw
		l>>= 1
		
	print("res after 2nd while loop = " + res)
	print("in hex: " + str(res.encode().hex()))
	print("\n")

	hashedres = hashlib.md5(res.encode()).hexdigest() # hash concatenated version of res
	
	print("hashedres = " + hashedres)
	#***************************************************************************
	
	
	
	#********************************** LOOP ***********************************
	
	for i in range(1000):
		tmp = "" 					# tmp str
		if i&1: tmp += pw
		else: tmp += hashedres # should this be hashed version or regular string?
		
		if i%3: tmp += salt
		
		if i%7: tmp += pw
	
		if i&1: tmp += hashedres
		else: tmp += pw
		
		hashedres = hashlib.md5(tmp.encode()).hexdigest()
	#***************************************************************************
	
	
	# testing purposes
	print("hashedres: " + hashedres + "\n")

#define magic
magic = "$1$"
# prompt user for input pw and salt
pw = input("Enter password: ")
salt = input("Enter salt: ")
print("\n")
encrypt(pw,salt,magic)



	
	