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
	
	res1comp = b'\x7a\x68\x67\x6e\x6e\x64\x24\x31\x24\x68\x66\x54\x37\x6a\x70\x32\x71\x3f\xfc\x86\xe7\xc7\x8f'
	
	if res == res1comp:
		print('res match')
	else:
		print('res no match')	
	
	
	l = len(pw) #reset l
	# For each bit in length(password), from low to high bits
	while l:
		print("l= " + str(l))
		if l & 1:
			res += b'\x00' # append null chr
		else:
			res += pw[0:1] # append first bit of pw
		l>>= 1 #shiftleft
		
	while2res = b'\x7a\x68\x67\x6e\x6e\x64\x24\x31\x24\x68\x66\x54\x37\x6a\x70\x32\x71\x3f\xfc\x86\xe7\xc7\x8f\x7a\x00\x00'
	if res == while2res:
		print('while2res match')
	else:
		print('res no match for while2res')	
		
	print("res after 2nd while loop = " + str(res))
	print("\n")

	hashedres = hashlib.md5(res).digest() # hash concatenated version of res
	
	print("hashedres = " + str(hashedres))
	
	# test strings
	compRes = b'\xed\x7a\x53\x07\x58\x8e\x49\xed\x3a\x27\x77\xd9\x26\xd6\x2f\x96'
	
	if hashedres == compRes:
		print('match')
	else:
		print('no match')
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
	
	finalrescomp = b'\xff\x20\x2f\x2e\x9b\x6a\xc6\xe4\x95\x57\x05\x36\xfc\x89\xfd\x2a'
	if hashedres == finalrescomp:
		print('final match')
	else:
		print('no final match')

#define magic
magic = b'$1$'
pw = b'\x7a\x68\x67\x6e\x6e\x64'
salt = b'\x68\x66\x54\x37\x6a\x70\x32\x71'
# prompt user for input pw and salt
#pw = input("Enter password: ")
#salt = input("Enter salt: ")
print("\n")
encrypt(pw,salt,magic)



	
	