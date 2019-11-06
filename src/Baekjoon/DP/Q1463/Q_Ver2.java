package Baekjoon.DP.Q1463;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q_Ver2 {

	public static void main(String[] args) {
		Q_Ver2 main = new Q_Ver2();
		main.init();
	}
	private int[] D = new int [100000000];
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			int N = Integer.parseInt(br.readLine().trim());
			D[0] = 0;
			D[1] = 0;
			D[2] = 1;
			for(int i=2; i<=N; i++){
				int temp = D[i-1] + 1;
				if(i%3 == 0)
					temp = Math.min(D[i/3] + 1, temp);
				if(i%2 == 0)
					temp = Math.min(D[i/2] + 1, temp);
				D[i] = temp;
			}
			
			System.out.println(D[N]);
			
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}
