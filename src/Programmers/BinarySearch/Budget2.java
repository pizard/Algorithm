package Programmers.BinarySearch;

import java.util.Arrays;

public class Budget2 {
	public static void main(String[] args) {
		int[] budgets = {5,5,5,15,25};
		double M = 50;

		
		Arrays.sort(budgets);
		int maxLength = budgets.length;		
		
		double averageNum = M/maxLength;
		
		int summaryLength = 0;
		int backwardSummary = 0;
		int forwardSummary = 0;
		
		int answer =  0;
		
		for(int number : budgets) {
			summaryLength++;
			forwardSummary += number;
			if(forwardSummary > averageNum*summaryLength) {
				break;
			}else {
				answer = number;
			}
			backwardSummary = forwardSummary;
		}
		
		if(forwardSummary > averageNum*summaryLength) {
			answer = (int)(M-backwardSummary)/(maxLength-summaryLength+1);
		}
		System.out.println(answer);
	}
}
