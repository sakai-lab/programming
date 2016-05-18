/*

3
メールアドレスを判定するスクリプトを正規表現を使って書け
メールアドレスは"@"によって前半後半に分けられ後半には"."が１つだけ含まれるものとする

*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

// 指定文字(char)delimiterで分割する関数
void split(vector<string> &v, const string &input_string,
	const char &delimiter) {
	string::size_type index = input_string.find_first_of(delimiter);

	if(index != string::npos) {
		v.push_back(input_string.substr(0, index));
		split(v, input_string.substr(index+1), delimiter);
	} else {
		v.push_back(input_string);
	}
}

int main() {
	string address;
	vector<string> v;
	vector<string> vl;

	// 入力
	cin >> address;

	split(v, address, '@');
	if(v.size() != 2) {
		cout << "'@'This is NOT an address." << endl;
		return 0;
	}

	split(vl, v[1], '.');
	if(vl.size() != 2) {
		cout << "'.'This is NOT an address." << endl;
		return 0;
	}

	cout << "This is an address." << endl;

	return 0;
}