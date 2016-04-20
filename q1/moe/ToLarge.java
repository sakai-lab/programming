/*
 "I am real sakai lab student"
    の各単語の頭文字をつなげて大文字にして出力するプログラムを書け

    文章を文字列型で定義して始めること
*/

public class ToLarge{
	public static void main(String[] args){
		String str = "I am real sakai lab student";
		String ans = "I";
		boolean check = false;
		char[] c = str.toCharArray();
		int i;
		for(i = 0; i < str.length(); i++){
			if(c[i] == ' ')check = true;
			else if(check){
				ans += String.valueOf(c[i]).toUpperCase();
				check = false;
			}
		}
		System.out.println(ans);
	}
}