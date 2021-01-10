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
	for i in range(hashedAlternateSum):
		intermidiateSum += hashedAlternateSum[i:passwordLength]
		
	# For each bit in length(password), from low to high and stopping after the most signicant set bit
	for i in passwordLength:
		if i & 1:
			#append null byte
		else:
			#append 1st pw byte
			intermidiateSum += pw[0:1]
	
	# hash final concatenated version of int sum
	hashedIntermidiateSum = hashlib.md5(intermidiateSum.encode('utf-8')).hexdigest()
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



	
	