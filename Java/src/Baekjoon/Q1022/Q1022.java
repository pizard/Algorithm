package Baekjoon.Q1022;

import java.util.Scanner;

public class Q1022 {
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int r1 = scan.nextInt();
		int c1 = scan.nextInt();
		int r2 = scan.nextInt();
		int c2 = scan.nextInt();
		int digit=0;
		int q1 = peak(r1,c1), q2 = peak(r1,c2), q3 = peak(r2,c1), q4 = peak(r2,c2);
		do{
			q1 = q1/10;
			q2 = q2/10;
			q3 = q3/10;
			q4 = q4/10;
			digit++;
		}while(q1 != 0 || q2 != 0 || q3 != 0 || q4 != 0);
		
		String[] result_S = new String[r2-r1+1];
		int[][] result = new int[r2-r1+1][c2-c1+1];
		for(int i=0; i<r2-r1+1;i++){
			for(int j=0; j<c2-c1+1;j++){
				result[i][j] = peak(r1+i,c1+j);
			}			
		}
		for(int i=0; i<r2-r1+1;i++){
			for(int j=0; j<c2-c1+1;j++){
				if(result_S[i] == null){
					result_S[i] = String.format("%"+digit+"d ", result[i][j]);
				}else{
					result_S[i] += String.format("%"+digit+"d ", result[i][j]);					
				}
			}
		}
		for(int i=0; i<r2-r1+1;i++){
			System.out.println(result_S[i]);			
		}
		
		scan.close();
	
	}

	
	public static int peak(int x, int y){
		int abs_x = Math.abs(x);
		int abs_y = Math.abs(y);
		int criteria = (abs_x > abs_y) ? abs_x : abs_y;
		int result = -1;
		
		int starting = (criteria * 2 - 1) * (criteria * 2 - 1);

		if(x < y){
			if(abs_x <= abs_y){
				// A
				result = starting + abs_y - x;
			}else{
				// B
				result = starting + abs_x * 2 + abs_x - y;
			}
		}else{
			if(abs_x <= abs_y){
				// C
				if( x == y&&x>0)					
					result = starting + (abs_x * 2) * 3 + abs_x + y;
				else
					result = starting + (abs_y * 2) * 2 + abs_y + x;
			}else{
				// D
				result = starting + (abs_x * 2) * 3 + abs_x + y;
			}
		}
		return result;
	}
	
}
