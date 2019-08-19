package DP.Q10844;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q10844 {

	public static void main(String[] args) {
		Q10844 main = new Q10844();
		main.init();
	}
	
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			int N = Integer.parseInt(br.readLine().trim());
			int[] digit = new int[N];
			int limit = 1;
			int count = 0;
			for(int i=0; i<N; i++){
				limit = limit * 10;
			}
			
			for(int i=(limit/10); i<limit; i++){
				int check = i;
				boolean result = true;
				for(int j=0; j<N; j++){
					digit[j] = check%10;
					check = check/10;
				}
				for(int j=0; j<N-1; j++){
					if(Math.abs(digit[j]-digit[j+1]) != 1)
						result = false;
				}
				if(result == true){
					count++;
				}
			}
			System.out.println(count%1000000000);
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}

/*
 * 10 12
 * 21 23
 * 32 34
 * 43 45
 * 54 56
 * 65 67
 * 76 78
 * 87 89
 * 98
*/

