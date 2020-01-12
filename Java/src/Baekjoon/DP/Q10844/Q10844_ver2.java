package Baekjoon.DP.Q10844;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q10844_ver2 {

	public static void main(String[] args) {
		Q10844_ver2 main = new Q10844_ver2();
		main.init();
	}
	
	private void init(){
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			int N = Integer.parseInt(bf.readLine().trim());
			long d[][] = new long[101][10];
			for(int i=1; i<=9; i++)
				d[1][i] = 1;
			for(int i=2; i<N+1; i++){
				for(int j=0; j<10; j++){
					if(j == 0)
						d[i][j] = d[i-1][j+1];
					else if(j==9)
						d[i][j] = d[i-1][j-1];
					else
						d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % 1000000000;
				}
			}
			
			long ans = 0;
			for(int i=0; i<10; i++){
				ans += d[N][i];
			}
			ans = ans%1000000000;
			System.out.println(ans);
			
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
