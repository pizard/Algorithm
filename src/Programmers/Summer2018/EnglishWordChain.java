package Programmers.Summer2018;

import java.util.ArrayList;

public class EnglishWordChain {
	public static void main(String[] args) {
		String[] words = {"hello", "one", "even", "never", "now", "world", "draw"};
		int n = 2; 
		ArrayList<String> wordSet = new ArrayList<String>();

		
		String lastChar = "";
		boolean result = true;
		String resultWord = "";
		
		int count = 1;
		for(String word : words) {
			if(!(lastChar.equals(word.substring(0,1)) || "".contentEquals(lastChar))) {
				resultWord = word;
				result = false;
				break;
			}
			if(wordSet.contains(word)) {
				resultWord = word;
				result = false;
				break;
			}
			wordSet.add(word);
			lastChar = word.substring(word.length()-1);
			count++;
		}
		
		
		
		int[] answer = new int[2];
		if( result ==true) {
			// 성공
			answer[0] = 0;
			answer[1] = 0;
		}else {
			// 실패
			if(count%n == 0) {
				answer[0] = n;
			}else {
				answer[0] = count%n;
			}
			answer[1] = (count+n-1)/n;
		}
		
		System.out.println(answer[0]);
		System.out.println(answer[1]);
		System.out.println(resultWord);
		System.out.println(count);
		System.out.println(result);
		
		
	}
}
