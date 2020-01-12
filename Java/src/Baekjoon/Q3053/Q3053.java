package Baekjoon.Q3053;

import java.util.Scanner;

public class Q3053 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int r = s.nextInt();
		System.out.printf("%.6f",r*r*Math.PI);
		System.out.println();
		System.out.println(r*r*2);
		s.close();
	}
}
