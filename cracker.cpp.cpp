//============================================================================
// Name        : bryce
// Version     :
// Copyright   :
// Description :
//============================================================================
#include <iostream>
#include<string>
//need md5 lib
using namespace std;

string initialization(string pw, string salt, string magic)
{
	string h;
	string res;
	int l;

	res = pw + magic + salt;
	//h = md5(pw + salt + pw); --  ** need to get md5 lib working **
	l = pw.length();

	while(l>0)
	{
		res = res + h.substr(0,min(16,l));
		l = l - 16;
	}

	for(int i = 0; i < pw.length(); i++)
	{

	}

	return res;
}


string hashfunction(string hash, string password, string salt)
{

	//loop - 1000 loops to compute complex hash
	//For i = 0 to 999 (inclusive), compute Intermediatei+1 by concatenating and hashing the following:
	//If i is even, Intermediate
	//If i is odd, password
	//If i is not divisible by 3, salt
	//If i is not divisible by 7, password
	//If i is even, password
	//If i is odd, Intermediatei
	//At this point you don’t need Intermediatei anymore.

	return hash;
}


int main() {

	string salt,password,hash,intermediate;
	string magic = "$1$";
	string res = "";

	cout << "enter user password: ";
	cin >> password;
	cout  << endl;

	cout << "enter salt: ";
	cin >> salt;
	cout  << endl;

	res = initialization(password, salt, magic);
	hash = hashfunction(res, password, salt);



	//finalization - convert to 64


	cout << intermediate << endl;
	return 0;
}





