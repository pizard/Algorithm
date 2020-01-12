package Programmers.BinarySearch;

import java.util.Arrays;

public class Budget {
	public static void main(String[] args) {
		int[] budgets = {120, 110, 140, 150};
		int M = 485;
		Arrays.sort(budgets);
		int maxLength = budgets.length;
		int checkLength = (int) Math.ceil(maxLength/2);
		int checkIndex = maxLength-checkLength;
		
		// 5 -> 8 -> 6 -> 7
		// 1 2 3 4 5 6 7 8 9 10 11
		while(true) {

			

			checkLength = (int)Math.ceil(checkLength/2);
			if(true) {
				checkIndex = maxLength-checkLength;
			}else {
				checkIndex = maxLength+checkLength;
			}
		}
		
	}
	
	
	
}
 