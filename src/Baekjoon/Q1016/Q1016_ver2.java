package Baekjoon.Q1016;

import java.util.Scanner;

public class Q1016_ver2 {
	static int squreNum = 0;
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		
		int minNum = scan.nextInt();
		int maxNum = scan.nextInt();
		
		for(int i=2; (i*i) <=maxNum ; i++){
			int min = minNum / (i*i);
			if(min * i * i != minNum)
				min++;
			int max = maxNum / (i*i);
			squreNum += (max - min + 1);	
			System.out.println("i: " + i);
			System.out.println("max: " + max);
			System.out.println("min: " + min);
			System.out.println("squreNum: " + squreNum);
		}
		System.out.println("result: " + (maxNum-minNum+1-squreNum));
		
		
		scan.close();
	}
}
