package Baekjoon.Q1028;

import java.util.Scanner;

public class Q1028 {
	static char[][] mine;
	static String[] mine_s;
	static int result = 0;
	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int R = scan.nextInt();
		int C = scan.nextInt();
		mine = new char[R][C];
		mine_s = new String[R];
		
		int checknum=(Math.max(R, C)+1)/2;

		scan.nextLine();

		for(int i=0; i<R; i++){
			mine_s[i] = scan.nextLine();
		}
		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				mine[i][j] = mine_s[i].charAt(j);
			}
		}
		
		
		for(; checknum != 0; checknum--){
			for(int i=checknum-1;i <= R-checknum; i++){
				for(int j=checknum-1; j <= C-checknum; j++ ){
					dig(i,j,checknum);
					if(checknum == result)
						break;
				}
				if(checknum == result)
					break;			
			}
			if(checknum == result)
				break;
		}
		
		System.out.println(result);
		scan.close();
	}
	
	public static void dig(int R, int C, int size){
		int tmp = result;
		result = size;
		
		for(int i=0; i<size;i++){
			if(mine[R-(size-1)+i][C-i] == '0' || mine[R+(size-1)-i][C+i] == '0' || mine[R-i][C+(size-1)-i] == '0' || mine[R+i][C-(size-1)+i] == '0'){
				result = tmp;
                break;
            }
		}
		
	}
}
