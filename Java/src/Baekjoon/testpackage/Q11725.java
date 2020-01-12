package Baekjoon.testpackage;

import java.util.Scanner;

public class Q11725 {
	static int node[][];
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		node = new int [N][3];
		
		for(int i=0; i<N-1; i++){
			node[i][0] = scan.nextInt();
			node[i][1] = scan.nextInt();
		}
		aaa(1,N);
		
		for(int i=2; i<=N; i++){
			for(int j=0;j<N-1;j++){
				if(node[j][1] == i){
					System.out.println(node[j][0]);
				}
					
			}
		}
		scan.close();
	}
	
	public static void aaa(int val, int N){
		int tmp =-1;
		for(int i=0; i<N-1; i++){
			if(node[i][2] == 0 && node[i][1] == val){
				tmp = node[i][1];
				node[i][1] = node[i][0];
				node[i][0] = tmp;
				node[i][2] = 1;
				aaa(node[i][1], N);
			}else if (node[i][2] == 0 && node[i][0] == val){
				node[i][2] = 1;
				aaa(node[i][1], N);
			}
		}
	}
}
