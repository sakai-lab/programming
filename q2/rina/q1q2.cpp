/*

1
data.txtに書かれているデータを読み込んで
member[名前]["weight"],member[名前]["height"]で
身長、体重にアクセス出来る連想配列を作れ
ただし、data.txtのデータは"名前,身長,体重"となっている

2
1で作成した連想配列を用いて名前を入力すると
その人のBMI(体重/(身長(m)×身長(m)))が出力される"関数"を書け

*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

// q2-BMIを返す関数
double returnBMI(map<string, map<string, double> > m, string mem) {
	return m[mem]["weight"]/(m[mem]["height"]*m[mem]["height"])*10000;
}

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

	ifstream ifs("data.txt");
	istringstream is;
	string str, delimiter;
	vector<string> v;
	map<string, map<string, double> > member;
	int i;
	string name;

	// file読み取り失敗
	if(ifs.fail()) {
		cerr << "ERROR" << endl;
		return -1;
	}

	while(getline(ifs, str)) {
		v.clear();
		split(v, str, ',');
		is.clear();
		is.str(v[1]);
		is >> member[v[0]]["height"];
		is.clear();
		is.str(v[2]);
		is >> member[v[0]]["weight"];
	}

	/*
	// q1-出力
	cout << "sato" << "\t" <<member["sato"]["height"]
		<< "\t" << member["sato"]["weight"] << endl;

	cout << "suzuki" << "\t" << member["suzuki"]["height"]
		<< "\t" << member["suzuki"]["weight"] << endl;

	cout << "kimura" << "\t" << member["kimura"]["height"]
		<< "\t" << member["kimura"]["weight"] << endl;

	cout << "uchimura" << "\t" << member["uchimura"]["height"]
		<< "\t" << member["uchimura"]["weight"] << endl;
	*/

	cout << "type name" << endl;
	while(cin >> name) {
		if(name=="end") break;
		cout << returnBMI(member, name) << endl;
	}

	return 0;
}
