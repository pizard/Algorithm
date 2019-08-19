package testpackage;

import java.util.Scanner;

public class Q1007 {
	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int T = scan.nextInt();
		int N, counting = 1, sumx = 0, sumy = 0;
		for(int i = 0; i<T; i++){
			N = scan.nextInt();
			int[][] P = new int [N][2];
			// ÁÂÇ¥ÀÔ·Â
			for(int j=0; j<N; j++){
				P[j][0] = scan.nextInt();
				P[j][1] = scan.nextInt();
				sumx += P[j][0];
				sumy += P[j][1];
				
				// °öÇÏ±â?
				counting = counting * (j+1);
				
			}
			
		}
	}

}
