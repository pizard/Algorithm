package Programmers.Greedy;

public class MakeBigNumber {
	public static void main(String[] args) {
		int k = 4;
		String number = "4177252841";
				
		int bigNum = -1;
		int bigNumLoc = -1;
		for(int i=0; i<k; i++) {
			for(int j=0; j<number.length(); j++) {
				
				String temp = number.substring(0,j)+number.substring(j);
				System.out.println(temp);
				System.out.println(temp.length());
				
				int currNum = Integer.parseInt(temp);
				if(currNum > bigNum) {
					bigNum = currNum;
					bigNumLoc = j;
				}
			}
			number = String.valueOf(bigNum);
		}
		
	
		
		System.out.print("@@@@");
		System.out.print(number);
		
		
		// 41772 > 최대 숫자 선택 : 7 -> 41 + 77
		// 252 > 최대 숫자 선택 : 5 -> 2 + 52
		// 52 > 최대 숫자 선5 + 2
		
	}
}



