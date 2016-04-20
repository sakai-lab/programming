/*
   if.swichなどの条件文を用いずに
    「sakai」が入力されたら「tetsuya」
    「nakajima」が入力されたら「tatsuo」
    「washizaki」が入力されたら「hironori」
    を出力するプログラムを書け

*/

import java.util.Scanner;
public class NotIf{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String s;
		while((s = sc.next()) != null){
			System.out.print(s.equals("sakai") ? "tetsuya" : "");
			System.out.print(s.equals("nakajima") ? "tatsuo" : "");
			System.out.print(s.equals("washizaki") ? "hironori" : "");
			System.out.println();
		}	
	}
}