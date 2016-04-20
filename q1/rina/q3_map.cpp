/*

q3
    if.swichなどの条件文を用いずに
    「sakai」が入力されたら「tetsuya」
    「nakajima」が入力されたら「tatsuo」
    「washizaki」が入力されたら「hironori」
    を出力するプログラムを書け

*/

#include <iostream>
#include <string>
#include <cstring>
#include <map>

using namespace std;

int main(void) {

	string str;

	map <string, string> mp;

	mp["sakai"] = "tetsuya";
	mp["nakajima"] = "tatsuo";
	mp["washizaki"] = "hironori";

	cin >> str;
	cout << mp[str] << endl;

	return 0;
}
