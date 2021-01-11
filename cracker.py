import sys
import hashlib #library to implement md5

def encrypt(pw, salt,magic):
	#initialization
	#***************************************************************************
	alternateSum = pw + salt + pw #get altsum
	hashedAlternateSum = hashlib.md5(alternateSum.encode('utf-8')).hexdigest()
	res = pw + magic + salt		#compute the intermidiate sum
	l = len(pw)	# get len(pw) -- should be 6 in our case
	
	# append length of password of hashed alt sum to res
	while l > 0:
		res = res + hashedAlternateSum[0:min(16,l)]
		l = l - 16
		
	l = len(pw) #reset l
	
	# For each bit in length(password), from low to high and stopping after the most signicant set bit
	while l:
		if l & 1:
			res += '\x00' # append null chr
		else:
			res += pw[0:1] # append first bit of pw
		l >>= 1
	
	# hash final concatenated version of int sum
	hashedres = hashlib.md5(res.encode('utf-8')).hexdigest()
	#***************************************************************************
	
	
	
	#********************************** LOOP ***********************************
	loopres = "" # str for loop intermidiate
	for i in range(1000):
		if i&1: loopres += pw
		else: loopres += hashedres # should this be hashed version or regular string?
		
		if i%3: loopres += salt
		
		if i%7: loopres += pw
	
		if i&1: loopres += hashedres
		else: loopres += pw
		
		hashedres = hashlib.md5(loopres.encode('utf-8')).hexdigest()
	#***************************************************************************
	
	
	# testing purposes
	print("hashed alternate sum: " + hashedAlternateSum + "\n")
	print("hashed intermidate sum: " + hashedres + "\n")

#define magic
magic = "$1$"
# prompt user for input pw and salt
pw = input("Enter password: ")
salt = input("Enter salt: ")
print("\n")
encrypt(pw,salt,magic)



	
	