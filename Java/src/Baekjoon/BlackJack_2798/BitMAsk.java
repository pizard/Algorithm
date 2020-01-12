package Baekjoon.BlackJack_2798;

public class BitMAsk {

	public static void main(String[] args) {

		System.out.println("---------------------------");

		int N = 5;
		int M = 21;
		int N_List[] = {5, 6, 7, 8, 9};

		for(int i=0;i<(1<<5);i++) {
			// 0,1,2,3,4...7
		    if(Integer.bitCount(i)==2) {
		    	// bit가 1인 갯수 출력
		    	// 11 > 3, 101 > 5, 110 > 6
		        for(int j=0;j<3;j++) {
		        	// 0, 1, 2
		            if(((1<<j)&i)>0) {
		            	// 1, 10, 10
		                System.out.print(j+"       ");
		            }
		        }
		        System.out.println();
		    }
		}
		
		
		for(int i=0;i<(1<<3);i++) {
		    System.out.println(i);
		}
		
		
		System.out.println("---------------------------");
		
		for(int i=0;i<(1<<3);i++) {
			// 0,1,2,3,4...7
		    if(Integer.bitCount(i)==2) {
		    	// bit가 1인 갯수 출력
		    	// 11 > 3, 101 > 5, 110 > 6
		        for(int j=0;j<3;j++) {
		        	// 0, 1, 2
		            if(((1<<j)&i)>0) {
		            	// 1, 10, 10
		                System.out.print(j+"       ");
		            }
		        }
		        System.out.println();
		    }
		}
		
	 
		
	}
}
