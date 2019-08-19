package Programmers.Hash;

import java.util.Arrays;

public class NotCompleteAth {
	public static void main(String[] args) {
		String[] phone_book = {"119", "97674223", "1195524421"};
		boolean result = true;
		Arrays.sort(phone_book);
		for(int i=0; i<phone_book.length-1;i++) {
			
			if(phone_book[i] == phone_book[i+1].substring(0,phone_book[i].length())) {
				result = false;
			}
		}
		
		System.out.println(result);
	}

}