package Baekjoon.BlackJack_2798;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int minNum = sc.nextInt();
		int maxNum = sc.nextInt();
		
		int maxSqrt = (int) Math.ceil(Math.sqrt(maxNum));
		
		boolean decimals[] = new boolean[maxNum+1];
		
		int result = 0;
		for(int i = 2; i<=maxSqrt; i++) {
			if(decimals[i] == false) {
				for(int j=2; minNum <=Math.pow(i, j) && Math.pow(i,j)<=maxNum; j++) {
					decimals[(int)Math.pow(i,j)] = true;
					result++;
				}
				for(int j=2; i*j<maxNum; j++) {
					decimals[i*j] = true;
				}
			}
		}
		System.out.println(result);
	}
}
