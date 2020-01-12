package Baekjoon.DP.Q2579;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q2579 {

	private int Max(int a, int b){
		return a>b ? a:b;
	}
	public static void main(String[] args) {
		Q2579 main = new Q2579();
		main.init();
		
	}
	// �Ѱ�� or �ΰ��
	// ���ӵ� 3���� ��� X
	// ������ ��� �ʼ�!
	private int[] step;
	private int[][] result;
	
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			int N = Integer.parseInt(br.readLine().trim());
			step = new int[N];
			result = new int[N][2];
			for(int i=0; i<N; i++){
				step[i] = Integer.parseInt(br.readLine().trim());
			}
			result[0][0] = step[0];
			result[0][1] = step[0];
			result[1][0] = step[0] + step[1];
			result[1][1] = step[1];
			
			for(int i=2; i<N; i++){
				result[i][0] = result[i-1][1] + step[i];
				result[i][1] = Max(result[i-2][0], result[i-2][1]) + step[i];
			}

			System.out.println(Max(result[N-1][0],result[N-1][1]));
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}
