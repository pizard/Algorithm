package Baekjoon.DP.Q1932;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q1932 {

/*
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5	
*/
	
	public static void main(String[] args) {
		Q1932 main = new Q1932();
		main.init();
	}
	
	private int N;
	private int tower[][];
	private void init() {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try { 
			N = Integer.parseInt(br.readLine().trim(), 10);
			tower = new int[N+1][N+1];
			for(int i=1; i<N+1; i++){
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				int count = 1;
				while(st.hasMoreTokens()){
					tower[i][count] = Integer.parseInt(st.nextToken().trim(),10);
					count++;
				}
			}
			for(int i=2; i<N+1; i++){		// 2 ~ N
				tower[i][1] = tower[i-1][1] + tower[i][1];
				tower[i][i] = tower[i-1][i-1] + tower[i][i];
/*				System.out.print(tower[i][1] + " ");*/
				for(int j=2; j<i; j++){		// 2 ~ i-1, (3,2)
					tower[i][j] = maxNum(tower[i-1][j-1]+tower[i][j], tower[i-1][j]+tower[i][j]);
/*					System.out.print(tower[i][j] + " ");*/
				}
/*				System.out.print(tower[i][i] + " ");
				System.out.println();*/
			}
			int result = tower[N][1];
			for(int i=1;i<N+1; i++)
				if(result < tower[N][i])
					result = tower[N][i];
			
			System.out.println(result);
			
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	private int maxNum(int num1, int num2){
		int result = num1 > num2 ? num1 : num2;
		return result;
	}
}
