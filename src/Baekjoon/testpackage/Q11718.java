package Baekjoon.testpackage;

import java.util.Scanner;

public class Q11718 {


	public static void main(String[] args){
	    Scanner scan = new Scanner(System.in);
	    int A = scan.nextInt();
	    int weight_5=-1, weight_3=-1,q,w,e;
	    q = A%5;
	    w = A/5;
	    switch (q){
			case 0:
				weight_5 = w;
				weight_3 = 0;
				break;
			case 1:
				weight_5 = w - 1;
				weight_3 = 2;
				break;
			case 2:
				weight_5 = w-2;
				weight_3 = 4;
				break;
			case 3:
				weight_5 = w;
				weight_3 = 1;
				break;
			case 4:
				weight_5 = w-1;
				weight_3 = 3;
				break;
	    	default:
	    		System.out.println("error");
	    		break;
	    }
	    
	    if(weight_5<0 || weight_3<0){
	    	System.out.println("-1");
	    }else{
	    	System.out.println(weight_5 + weight_3);
	    }
	    	
	    	
	    	
	    	
	    scan.close();
	}    
}
