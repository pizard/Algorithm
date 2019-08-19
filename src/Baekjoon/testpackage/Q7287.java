package testpackage;

import java.util.Scanner;

public class Q7287 {

	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int roopCount = scan.nextInt();
		for(;roopCount > 0; roopCount--){
		// Roop Start
		int towerNum, towerBuildRuleNum, startPoint, endPoint, goalPoint;

		System.out.println("---------------- towerNum, towerBuildRuleNum ----------------");
		towerNum = scan.nextInt();
		towerBuildRuleNum = scan.nextInt();

		int[] towerBuildTime = new int [towerNum];
		int[] baseTowerBuildTime = new int [towerNum];
		int[] test = new int [towerNum];

		System.out.println("---------------- towerBuildTime ----------------");
		for(int counting = 0;counting<towerNum;counting++){
			towerBuildTime[counting] = scan.nextInt();			
			baseTowerBuildTime[counting] = towerBuildTime[counting];
		}
		
		System.out.println("---------------- towerBuildRule ----------------");
		for(;towerBuildRuleNum>0; towerBuildRuleNum--){
			startPoint = scan.nextInt();
			endPoint = scan.nextInt();
			if((towerBuildTime[endPoint-1]-baseTowerBuildTime[endPoint-1]) < towerBuildTime[startPoint-1]){
				towerBuildTime[endPoint-1] = towerBuildTime[startPoint-1] + baseTowerBuildTime[endPoint-1];				
			}			
		}
		
		System.out.println("---------------- goalPoint ----------------");
		goalPoint = scan.nextInt();
		
		System.out.println("---------------- °á°ú ----------------");
		System.out.println(towerBuildTime[goalPoint-1]);
		}
		
		scan.close();
	}

}
