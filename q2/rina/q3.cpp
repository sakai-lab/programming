/*

3
メールアドレスを判定するスクリプトを正規表現を使って書け
メールアドレスは"@"によって前半後半に分けられ後半には"."が１つだけ含まれるものとする

*/

#include <iostream>
#include <regex>
#include <string>

using namespace std;


int main() {
	string input;
	smatch match;
	regex re("^(.@)+@[^(.@)]+.[^(.@)]+");

	// 入力
	cin >> input;



	if(regex_match(input, match,re)) {
		cout << "This is an address." << endl;
	} else {
		cout << "This is NOT an address." << endl;
	}

	return 0;
}