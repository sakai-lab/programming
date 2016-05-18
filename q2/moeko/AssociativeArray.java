/*
data.txtに書かれているデータを読み込んで
member[名前]["weight"],member[名前]["height"]で身長、体重にアクセス出来る連想配列を作れ
ただし、data.txtのデータは"名前,身長,体重"となっている
*/

import java.util.HashMap;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileNotFoundException;

public class AssociativeArray{
	public static void main(String[] args){
		HashMap<String, HashMap<String, Double>> map = new HashMap<String, HashMap<String, Double>>();
		try{
			BufferedReader reader = new BufferedReader(new FileReader("../data.txt"));
			String s = reader.readLine();
			while(s != null){
				String[] strs = s.split(",", 0);
				map.put(strs[0], new HashMap<String, Double>());
				map.get(strs[0]).put("height", Double.parseDouble(strs[1]));
				map.get(strs[0]).put("weight", Double.parseDouble(strs[2]));
				s = reader.readLine();
			}
		}catch(FileNotFoundException e){
			System.out.println(e);
		}catch(IOException e){
			System.out.println(e);
		}
		System.out.println(map.get("sato").get("height"));
		System.out.println(map.get("uchimura").get("weight"));
	}
}


