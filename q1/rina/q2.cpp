/*

q2
    入力された文字列(.と数字の連続)が
    IPv4で定義された範囲のIPアドレス(***.***.***.***)
    になりえるかどうか判定するプログラムを書け
    なお文字列はコマンドライン引数から1つ指定するものとする

*/

#include <iostream>
#include <string>
#include <cstring>

#define NUM 0
#define DOT 1

using namespace std;

int main() {

	int i;
	int p=0;
	int prec=DOT;
	int nowc=DOT;
	bool flag=true;
	char str[101];

	cin >> str;

	i=0;
	while(str[i]!='\0') {
		if(str[i]>='0' && str[i]<='9') nowc=NUM;
		else nowc=DOT;

		if(nowc==DOT) {
			if(prec==DOT) {
				flag = false;
				break;
			} else { // prec==NUM; 
				if(p<0 || p>255) {
					flag=false;
					break;
				}
			}
		}

		else if(nowc==NUM) {
			if(prec==DOT) {
				p=str[i]-'0';
			} else {
				p = p*10 + (str[i]-'0');
			}
		}

		prec = nowc;
		i++;
	}


	if(flag) cout << "True" << endl;
	else cout << "False" << endl;

	return 0;



	return 0;
}
