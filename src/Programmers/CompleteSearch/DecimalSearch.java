package Programmers.CompleteSearch;

import java.util.ArrayList;
import java.util.Scanner;

public class DecimalSearch {
	static int result = 0;
	static boolean decimals[];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String numbers = sc.nextLine();
		int length = numbers.length();
		int numbersArray[] = new int[10];
		
		
		ArrayList<Integer> numbersList = new ArrayList<Integer>();
		for(int i=0; i<length; i++) {
			numbersList.add(Integer.parseInt(numbers.substring(i, i+1)));
			numbersArray[Integer.parseInt(numbers.substring(i, i+1))]++;
		}
		
		/* 소수 배열 만들기!! */
		int maxNum = (int) Math.pow(10, length);
		
		decimals = new boolean[maxNum];
		
		// false : 소수, true : 합성수
		for(int i = 2; i<maxNum; i++) {
			// 소수 인 경우
			if(decimals[i] == false) {
				// 합성수 제거
				for(int j=2; i*j<maxNum; j++) {
					decimals[i*j] = true;
				}
			}
		}
		decimals[1] = true;
		checkDecimals(0, numbersArray);
		
		System.out.println(result);
	}
	
	
	public static void checkDecimals(int nubmer, int[] numbersArray) {
		for(int i=0; i<10; i++) {
			if(numbersArray[i] != 0) {
				int checkNum = nubmer * 10 + i;
				int[] checkNumbersArray = numbersArray;
				checkNumbersArray[i] = checkNumbersArray[i]-1;
				
				if(decimals[checkNum] == false) {
					decimals[checkNum] = true;
					System.out.println(checkNum);
					result++;
				}
				checkDecimals(checkNum, checkNumbersArray);
			}
		}
	}
	
	public static void checkDecimals2(int nubmer, int[] numbersArray) {
		for(int i=0; i<10; i++) {
			if(numbersArray[i] != 0) {
				int checkNum = nubmer * 10 + i;
				int[] checkNumbersArray = numbersArray;
				if(decimals[checkNum] == false) {
					decimals[checkNum] = true;
					checkNumbersArray[i] = checkNumbersArray[i]-1;
					result++;
					checkDecimals2(checkNum, checkNumbersArray);
				}

			}
		}
	}
}