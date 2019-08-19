package graph.Q7576;

import java.util.Scanner;

public class Q7576_v2 {
	static int[][] box;
	static int[][] checkingbox;
	static int M,N, count=0, checkNum=0;
	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		N = scan.nextInt();
		M = scan.nextInt();
		box = new int[M][N];
		checkingbox = new int[M][N];
		
		int tomatoNum = 0;
		
		for(int i=0;i<M; i++){
			for(int j=0; j<N; j++){
				box[i][j] = scan.nextInt();
				if(box[i][j] == 1){
					count++;
					tomatoNum++;
				}else if(box[i][j]== 0){
					tomatoNum++;
				}
			}
		}
		
		
		if(count==0)
			// 다 익을 수 없는 경우
			System.out.println("-1");
		else if(count == tomatoNum){
			// 다 익어있는 경우
			System.out.println("0");
		}else{
			for(int i=0;i<M+N-1;i++){
				for(int j=0;j<N;j++){
					for(int k=0;k<M;k++){
						if(box[j][k] == 1 && checkingbox[j][k] == 0){
							injection(j,k);
							checkingbox[j][k] = 1;
						}
					}
				}
			}
			
			if(tomatoNum != checkNum)
				System.out.println("-1");
			else
				System.out.println(count);
		}
		
		
		
		
		
		scan.close();
	
	}
	
	
	static void injection(int m, int n){
		int check =0;
		if(m+1<M){
			if(box[m+1][n] == 0){
				box[m+1][n] =1;
				check = 1;
				checkNum++;  
			}
		}
		if(m-1>-1){
			if(box[m-1][n] == 0){
				box[m-1][n] =1;
				check = 1;
				checkNum++;  
			}
		}
		if(n+1<M){
			if(box[m][n+1] == 0){
				box[m][n+1] =1;
				check = 1;
				checkNum++;  
			}
		}
		if(n-1>-1){
			if(box[m][n-1] == 0){
				box[m][n-1] =1;
				check = 1;
				checkNum++;  
			}
		}
		
		if(check ==1)
			count++;
	}
}
