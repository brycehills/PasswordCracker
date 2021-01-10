import sys
import hashlib #library to implement md5

def encrypt(pw, salt):

	#initialization
	alternateSum = pw + salt + pw
	alternateSum = hashlib.md5(alternateSum.encode('utf-8')).hexdigest()

	
	#compute the intermidiate sum
	intermidiateSum = pw + magic + salt
	intermidiateSum = hashlib.md5(intermidiateSum.encode('utf-8')).hexdigest()
	
	print("alternate sum: " + alternateSum + "\n")
	print("intermidate sum: " + intermidiateSum + "\n")

#define magic
magic = "$1$"

# prompt user for input pw and salt
pw = input("Enter password: ")
salt = input("Enter salt: ")
print("\n")

encrypt(pw,salt)



	
	