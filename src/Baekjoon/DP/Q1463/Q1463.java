package DP.Q1463;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q1463 {

	public static void main(String[] args) {
		Q1463 main = new Q1463();
		main.init();
	}
	
	private int count;
	private int result=100000000;
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			int N = Integer.parseInt(br.readLine().trim());
			solve(N,0);
			System.out.println(result);
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	
	private void solve(int N, int count){
		if(N==1){
			if(result > count)
				result = count;
		}else{
			if(N % 6 == 0){
				N = N-1;
				solve(N,(count+1));
			}else if(N % 3 == 0){
				N = N / 3;
				solve(N,(count+1));
			}else{
				if(N % 2 == 0){
					solve((N/2),(count+1));
				}
				solve((N-1),(count+1));
			}
		}
		
	}
}
