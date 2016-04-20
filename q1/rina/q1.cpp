/*

q1
    "I am real sakai lab student"
    の各単語の頭文字をつなげて大文字にして出力するプログラムを書け

    文章を文字列型で定義して始めること

*/

#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main() {

	int i;
	char str[101];

	for(i=0; i<6; i++) {
		cin >> str;
		if(str[strlen(str)]=='\n') break;
		if(str[0]>='A' && str[0]<='Z') cout << str[0];
		else cout << (char)(str[0]-'a'+'A');
	}

	cout << endl;

	return 0;
}