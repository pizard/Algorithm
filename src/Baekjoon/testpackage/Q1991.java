package testpackage;

import java.util.Scanner;

public class Q1991 {
	static char resultA;
	static char[][] node;
	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		node = new char[N][3];
		for(int i=0; i<N; i++){
			node[i][0] = scan.next().charAt(0);
			node[i][1] = scan.next().charAt(0);
			node[i][2] = scan.next().charAt(0);
		}
		// 전위순회
		aaa('A', N, 'a');
		System.out.println();
		aaa('A', N, 'b');
		System.out.println();
		aaa('A', N, 'c');
		scan.close();
	}
	
	public static void aaa(char sw, int N, char check){
		int count = -1;
		for(int i=0; i<N; i++){
			if(node[i][0] == sw){
				count = i;
				break;
			}
		}

		switch(check){
			case 'a':
				System.out.print(node[count][0]);
				if(node[count][1] != '.')
					aaa(node[count][1], N, check);
				if(node[count][2] != '.')
					aaa(node[count][2], N, check);
				break;
			case 'b':
				if(node[count][1] != '.')
					aaa(node[count][1], N, check);
				System.out.print(node[count][0]);
				if(node[count][2] != '.')
					aaa(node[count][2], N, check);
				break;
			case 'c':
				if(node[count][1] != '.')
					aaa(node[count][1], N, check);
				if(node[count][2] != '.')
					aaa(node[count][2], N, check);
				System.out.print(node[count][0]);
				break;
			default:
					break;
		}
		
	}
}
