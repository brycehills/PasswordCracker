import sys
import hashlib  # library to implement md5
import binascii # for hex conversion

def encrypt(pw, salt, magic):
  
	#*******************************initialization******************************
	alt = pw + salt + pw        #get alt
	res = pw + magic + salt		#compute res
	print("res = " + str(res))
	
	h = hashlib.md5(alt).digest()
	print("h = " + str(h))
	
	l = len(pw)	# get len(pw) -- should be 6 in our case
	print("l = " + str(l))
	
	while l > 0: #concat h to res for len(l)
		res = res + h[0:min(16,l)]
		l = l - 16
		
	print("\nres after 1st while loop = " + str(res))
	print("\n")
	
	l = len(pw) #reset l
	# For each bit in length(password), from low to high 
	while l:
		if l & 1:
			res += b'\x00' # append null chr
		else:
			res += pw[0:1] # append first bit of pw
		l>>= 1
		
	print("res after 2nd while loop = " + str(res))
	print("\n")

	hashedres = hashlib.md5(res).digest() # hash concatenated version of res
	
	print("hashedres = " + str(hashedres))
	#***************************************************************************
	
	
	
	#********************************** LOOP ***********************************
	
	for i in range(1000):
		tmp = b"" 					# tmp str
		if i&1: tmp += pw
		else: tmp += hashedres # should this be hashed version or regular string?
		
		if i%3: tmp += salt
		
		if i%7: tmp += pw
	
		if i&1: tmp += hashedres
		else: tmp += pw
		
		hashedres = hashlib.md5(tmp).digest()
	#***************************************************************************
	
	
	# testing purposes
	print("hashedres: " + str(hashedres) + "\n")

#define magic
magic = b'$1$'
pw=b'\x7a\x68\x67\x6e\x6e\x64'
salt=b'\x68\x66\x54\x37\x6a\x70\x32\x71'
# prompt user for input pw and salt
#pw = input("Enter password: ")
#salt = input("Enter salt: ")
print("\n")
encrypt(pw,salt,magic)



	
	