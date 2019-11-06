package Baekjoon.Q1026;

import java.util.Scanner;

public class Q1026 {
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int[] A = new int[N];
		int[] B = new int[N];
		for(int i=0; i<N; i++){
			A[i] = scan.nextInt();
		}
		for(int i=0; i<N; i++){
			B[i] = scan.nextInt();
		}
		int tmp = 0, tmp2 = 0;;
		for(int i=0; i<N-1; i++){
			for(int j = 0; j<N-i-1; j++){
				if(A[j]>A[j+1]){
					tmp = A[j];
					A[j] = A[j+1];
					A[j+1] = tmp;
				}
				if(B[j]<B[j+1]){
					tmp2 = B[j];
					B[j] = B[j+1];
					B[j+1] = tmp2;
				}
			}
		}
		int sum=0;
		for(int i=0; i<N; i++)
			sum +=A[i] * B[i];
		
		System.out.println(sum);
		
		scan.close();
	
	}
	
	
}
