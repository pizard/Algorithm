package Baekjoon.BlackJack_2798;

import java.util.Scanner;

public class Decimal {
	// 소수 : 1과 자기자신만 있는 경우
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int minNum = sc.nextInt();
		int maxNum = sc.nextInt();
		
		// int decimals[] = new decimals[maxNum];
		boolean decimals[] = new boolean[maxNum+1]; // false : 소수, true : 소수 x
		
		decimals[0] = true;
		decimals[1] = true;
		
		
		for(int i = 2; i<=maxNum; i++) {
			if(decimals[i] == false) {
				int j = 2;
				while(i*j<=maxNum) {
					decimals[i*j] = true;
					j++;
				}					
			}
		}
		
		int result = 0;
		for(int i=minNum; i<=maxNum; i++) {
			if(decimals[i] == false) {
				System.out.println(i);
				result++;
			}
		}
		
		System.out.println("------------------------------");
		System.out.println(result);
	}

}
