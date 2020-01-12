package Baekjoon.testpackage;

import java.util.Scanner;

public class Q1005_ver3_clear {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int T=0;
		T = scan.nextInt();
		
		int N=0, K=0,t_1=0,t_2=0,w=0;
		
		int[] ans = new int [1001];
		int[] DP;
		int[] num_Building;
		int[][] adj_matrix;
		
		
		for(int i=0; i<T; i++){
			num_Building = new int[1001];
			adj_matrix = new int[1001][1001];
			DP = new int[1001];

			
			N = scan.nextInt();
			K = scan.nextInt();
			
			for(int j = 1; j<=N; j++)
				num_Building[j] = scan.nextInt();
			
			for(int x =0; x<K; x++){
				t_1 = scan.nextInt();
				t_2 = scan.nextInt();
				adj_matrix[t_1][t_2] = 1;
			}
			w = scan.nextInt();
			
			ans[i] = dfs(adj_matrix, num_Building, DP, w, N);
		}
		
		for(int i=0;i<T; i++)
			System.out.println(ans[i]);
		
		scan.close();
	}
	
	
	public static int dfs(int[][] adj_matrix, int[] num_Building, int[] DP, int w, int N){
		int res = 0;
		int tmp = 0;
		
		if(DP[w] != 0) return DP[w];
		for(int i =1; i <= N ; i++){
			if(adj_matrix[i][w] ==1){
				res = dfs(adj_matrix,num_Building,DP,i,N);
				if(tmp < res){
					tmp = res;
				}
			}
		}
		
		int t = num_Building[w] + tmp;
		if(DP[w] < t) DP[w] = t;
		return t;
	}
	

}
