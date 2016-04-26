/*
入力された文字列(.と数字の連続)が
    IPv4で定義された範囲のIPアドレス(***.***.***.***)
    になりえるかどうか判定するプログラムを書け
    なお文字列はコマンドライン引数から1つ指定するものとする
*/

public class IPAddress{
	public static void main(String[] args){
		if(args.length != 1) return;
		String[] strs = args[0].split("\\.", 0);
		boolean ans = true;
		for(int i = 0; i < strs.length; i++){
			int s = Integer.parseInt(strs[i]);
			if(s > 255 || s < 0){
				ans = false;
				break;
			}
		}
		if(ans) System.out.println("It's IP Address");
		else System.out.println("It's not IP Address");
	}
}