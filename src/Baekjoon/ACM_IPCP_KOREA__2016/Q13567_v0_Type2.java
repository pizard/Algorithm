package Baekjoon.ACM_IPCP_KOREA__2016;

import java.util.Arrays;
import java.util.Scanner;

public class Q13567_v0_Type2 {
	public static void main(String... args) {
		Scanner input = new Scanner(System.in);
		int[] points = new int[input.nextInt()];
		boolean answer = true;
		int sum = 0;

		for (int index = 0; index < points.length; index++)
			points[index] = input.nextInt();

		Arrays.sort(points);
		
		for (int index = 0; index < points.length; index++) {
			sum += points[index];
			if (sum < (index + 1) * index / 2) {
				answer = false;
				break;
			}
		}

		System.out.print(sum == (points.length * (points.length - 1) / 2) && answer ? 1 : -1);
		input.close();
	}
}
