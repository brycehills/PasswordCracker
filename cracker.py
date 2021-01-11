import sys
import hashlib #library to implement md5

def encrypt(pw, salt,magic):
	#initialization
	#***************************************************************************
	#get altsum
	alternateSum = pw + salt + pw
	hashedAlternateSum = hashlib.md5(alternateSum.encode('utf-8')).hexdigest()

	#compute the intermidiate sum
	intermidiateSum = pw + magic + salt
	
	# get len(pw) in bytes
	passwordLength = len(pw.encode('utf-8'))
	
	# add length(password) bytes of the Alternate sum, repeated as necessary
	for i in range(len(hashedAlternateSum)):
		intermidiateSum += hashedAlternateSum[i:passwordLength]
		
	# For each bit in length(password), from low to high and stopping after the most signicant set bit
	for i in range(passwordLength):
		if i & 1:
			#append null byte - chr(0) is null char - not encoded at this point (Still str)
			intermidiateSum += chr(0)
		else:
			#append 1st pw byte - still string here
			intermidiateSum += pw[0:1]
	
	# hash final concatenated version of int sum
	hashedIntermidiateSum = hashlib.md5(intermidiateSum.encode('utf-8')).hexdigest()
	#***************************************************************************
	
	
	
	#********************************** LOOP ***********************************
	loopintermidiate = "" # str for loop intermidiate
	for i in range(1000):
		if i&1: loopintermidiate += pw
		else: loopintermidiate += hashedIntermidiateSum # should this be hashed version or regular string?
		
		if i%3: loopintermidiate += salt
		
		if i%7: loopintermidiate += pw
	
		if i&1: loopintermidiate += hashedIntermidiateSum
		else: loopintermidiate += pw
		
		hashedIntermidiateSum = hashlib.md5(loopintermidiate.encode('utf-8')).hexdigest()
	#***************************************************************************
	
	
	# testing purposes
	print("hashed alternate sum: " + hashedAlternateSum + "\n")
	print("hashed intermidate sum: " + hashedIntermidiateSum + "\n")

#define magic
magic = "$1$"
# prompt user for input pw and salt
pw = input("Enter password: ")
salt = input("Enter salt: ")
print("\n")
encrypt(pw,salt,magic)



	
	