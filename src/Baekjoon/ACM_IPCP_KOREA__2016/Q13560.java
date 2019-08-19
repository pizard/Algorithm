package ACM_IPCP_KOREA__2016;

import java.util.Scanner;

public class Q13560 {

	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int teamNum = scan.nextInt();
		int[] score = new int [teamNum];
		int checkPoint1 = 0;// ÃÑ Á¡¼ö
		int[] checkPoint2 = new int [teamNum];
		int result=0;
		
		
		for(int i=0; i<teamNum; i++){
			score[i] = scan.nextInt();
			checkPoint1 += score[i];
			checkPoint2[score[i]]++;
		}
		
		if(checkPoint1 != teamNum*(teamNum-1)/2){
			System.out.println("Point1");
			result = -1;
		}else{
			for(int i=0; i<teamNum/2 + teamNum % 2; i++){
				if((checkPoint2[i] > i*2+1) || (checkPoint2[teamNum-1-i] > i*2+1)){
					result = -1;
					break;
				}
			}
		}

		if(result == 0){
			System.out.println("1");				
		}else{
			System.out.println("-1");
		}
	}
}
