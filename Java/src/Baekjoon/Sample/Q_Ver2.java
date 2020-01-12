package Baekjoon.Sample;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_Ver2 {

	public static void main(String[] args) {
		Q_Ver2 main = new Q_Ver2();
		main.init();
	}
	
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			int N = Integer.parseInt(br.readLine().trim());
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}
