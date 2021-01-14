import sys
import hashlib  # library to implement md5
import binascii # for hex conversion

def initialization(pw, salt, magic):

	alt = pw + salt + pw
	res = pw + magic + salt
	
	h = hashlib.md5(alt).digest()
	
	l = len(pw)	# get len(pw) -- should be 6 in our case
	
	while l > 0: #concat h to res for len(l)
		res = res + h[0:min(16,l)]
		l = l - 16

	l = len(pw) #reset l
	# For each bit in length(password), from low to high bits
	while l:
		if l & 1:
			res += b'\x00' # append null chr
		else:
			res += pw[0:1] # append first byte of pw
		l>>= 1 				#shiftleft

	hashedres = hashlib.md5(res).digest() # hash concatenated version of res
	
	return hashedres
	

def loop(hashedres,pw,salt):
	for i in range(1000):
		tmp = b"" 					# tmp str
		if i&1: tmp += pw
		else: tmp += hashedres # should this be hashed version or regular string?
		
		if i%3: tmp += salt
		
		if i%7: tmp += pw
	
		if i&1: tmp += hashedres
		else: tmp += pw
		
		hashedres = hashlib.md5(tmp).digest()
		
	return hashedres
	
		
def finalization(pw,salt,magic,finalsum):
	return to64()


#define magic
magic = b'$1$'
pw = b'\x7a\x68\x67\x6e\x6e\x64'
salt = b'\x68\x66\x54\x37\x6a\x70\x32\x71'
res = b''
# prompt user for input pw and salt
#pw = input("Enter password: ")
#salt = input("Enter salt: ")
print("\n")
res = initialization(pw,salt,magic)
res = loop(res,pw,salt)
print(str(res))





	
	