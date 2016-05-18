/*
メールアドレスを判定するスクリプトを正規表現を使って書け
メールアドレスは"@"によって前半後半に分けられ後半には"."が１つだけ含まれるものとする
*/

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class MailAddress{
	public static void main(String[] args){
		if(args.length != 1) return;
		Pattern p = Pattern.compile("\\w+@[a-zA-Z]+\\.[a-zA-Z]+");
		Matcher m = p.matcher(args[0]);
		System.out.println(m.find());
	}
}