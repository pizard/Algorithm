package Baekjoon.BlackJack_2798;

import java.util.Scanner;

public class Almost_Decimal {

	// 소수 : 1과 자기자신만 있는 경우
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double minNum = sc.nextDouble();
		double maxNum = sc.nextDouble();

		
		int maxSqrt = (int) Math.ceil(Math.sqrt(maxNum));
		boolean decimals[] = new boolean[maxSqrt+1];		
		int result = 0;
		
		// false : 소수, true : 합성수
		// 1 ~ maxSqrt까지의 소수를 구할거야!!
		for(int i = 2; i<=maxSqrt; i++) {
			// 소수 인 경우
			if(decimals[i] == false) {
				// 합성수 제거
				for(int j=2; i*j<=maxSqrt; j++) {
					decimals[i*j] = true;
				}
			}
		}
		
		// i^j
		for(int i=2; i< (maxSqrt+1); i++) {
			if(decimals[i] == false) {
				for(double j=2; minNum <=Math.pow(i, j) && Math.pow(i,j)<=maxNum; j++) {
					result++;
				}
			}
		}

		System.out.println(result);
	}
}