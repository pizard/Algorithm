package Baekjoon.testpackage;

import java.util.Scanner;

public class Q1005_ver1 {
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
		int[][] towerBuildSequence = new int [towerNum][towerNum];
		
		System.out.println("---------------- towerBuildTime ----------------");
		for(int counting = 0;counting<towerNum;counting++){
			towerBuildTime[counting] = scan.nextInt();			
			baseTowerBuildTime[counting] = towerBuildTime[counting];
		}
		
		System.out.println("---------------- towerBuildRule ----------------");
		for(;towerBuildRuleNum>0; towerBuildRuleNum--){
			startPoint = scan.nextInt();
			endPoint = scan.nextInt();
			towerBuildSequence[startPoint-1][endPoint-1] = 1;
			/*if((towerBuildTime[endPoint-1]-baseTowerBuildTime[endPoint-1]) < towerBuildTime[startPoint-1]){
				towerBuildTime[endPoint-1] = towerBuildTime[startPoint-1] + baseTowerBuildTime[endPoint-1];				
			}*/
		}
		
		for(int countingX = 0; countingX <towerNum; countingX++ ){
			for(int countingY=0; countingY<countingX; countingY++){
				if(towerBuildSequence[countingX][countingY] == 1){
					System.out.println("[" + countingX + "][" + countingY+ "]");
				}
			}
		}
		
		
		System.out.println("---------------- goalPoint ----------------");
		goalPoint = scan.nextInt();
		
		System.out.println("---------------- ��� ----------------");
		System.out.println(towerBuildTime[goalPoint-1]);
		}
		
		scan.close();
	}
}
