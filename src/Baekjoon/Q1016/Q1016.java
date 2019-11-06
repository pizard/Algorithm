package Baekjoon.Q1016;

import java.util.Scanner;

public class Q1016 {
	static int squreNum = 0;
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);	///
		
		
		int minNum = scan.nextInt();
		int maxNum = scan.nextInt();
		
		
		for(int i=minNum; i<=maxNum;i++)
			checkDouble(i);
		
		System.out.println("squreNum: " + squreNum);
		System.out.println("result: " + (maxNum-minNum+1-squreNum));
		
		scan.close();
	}
	
	
	
	public static void checkDouble(int checkNum){
		int stand = (int) Math.sqrt(checkNum);
		int count;
		for(int i=2; i<=stand; i++){
			count =0;
			while(checkNum % i == 0){
				checkNum = checkNum/i;
				count++;
				if(count == 2){
					System.out.println(checkNum * i * i);
					squreNum++;
					break;
				}
			}
			if(count == 2)
				break;
		}
	}
}
