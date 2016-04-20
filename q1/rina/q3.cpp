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

using namespace std;

int main(void) {

	string ans[5] = {
		"tetsuya",
		"wrong",
		"wrong",
		"tatsuo",
		"hironori"
	};
	char str[10];

	cin >> str;
	cout << ans[strlen(str)-5] << endl;

	return 0;
}
