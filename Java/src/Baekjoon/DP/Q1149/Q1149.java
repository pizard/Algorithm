package Baekjoon.DP.Q1149;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q1149 {
	public static void main(String[] args) {
		Q1149 main = new Q1149();
		main.init();
	}
	
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			int N = Integer.parseInt(br.readLine().trim());
			int[][] buildCost = new int[N+1][3];
			int[][] minCost = new int[N+1][3];
			for(int i=1; i<N+1; i++){
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				buildCost[i][0] = Integer.parseInt(st.nextToken().trim());	// RED
				buildCost[i][1] = Integer.parseInt(st.nextToken().trim());	// GREEN
				buildCost[i][2] = Integer.parseInt(st.nextToken().trim());	// GREEN
			}
			
			minCost[1][0] = buildCost[1][0];
			minCost[1][1] = buildCost[1][1];
			minCost[1][2] = buildCost[1][2];
			
			for(int i=2; i<N+1; i++){
				minCost[i][0] = minNum(minCost[i-1][1] + buildCost[i][0], minCost[i-1][2] + buildCost[i][0]);
				minCost[i][1] = minNum(minCost[i-1][2] + buildCost[i][1], minCost[i-1][0] + buildCost[i][1]);
				minCost[i][2] = minNum(minCost[i-1][0] + buildCost[i][2], minCost[i-1][1] + buildCost[i][2]);
			}
			
			System.out.println(minNum(minCost[N][0], minCost[N][1], minCost[N][2]));
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
		
	private int minNum(int num1, int num2, int num3){
		int result = num1 < num2 ? num1 : num2;
		result = result < num3 ? result : num3;
		return result;
	}
	private int minNum(int num1, int num2){
		int result = num1 < num2 ? num1 : num2;
		return result;
	}
	
}
