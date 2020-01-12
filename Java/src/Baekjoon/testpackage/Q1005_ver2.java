package Baekjoon.testpackage;

import java.util.Scanner;

public class Q1005_ver2 {
	static int towerNum, result =0;
	static int[][] towerBuildSequence;
	static int[] towerBuildTime;
	static int[] baseTowerBuildTime;
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int roopCount = scan.nextInt();
		for(;roopCount > 0; roopCount--){
			// Roop Start
			int towerBuildRuleNum, startPoint, endPoint, goalPoint;
			
	
			System.out.println("---------------- towerNum, towerBuildRuleNum ----------------");
			towerNum = scan.nextInt();
			towerBuildRuleNum = scan.nextInt();
	
			
			towerBuildTime = new int [towerNum];
			baseTowerBuildTime = new int [towerNum];
			towerBuildSequence = new int [towerNum][towerNum];
			
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
			}
			
			System.out.println("---------------- goalPoint ----------------");
			goalPoint = scan.nextInt();
			aaa(goalPoint);
			
			
			
			System.out.println("---------------- ��� ----------------");
			System.out.println(result);
		
		}
		
		scan.close();
	}
	
	
	// val = endPoint, counting = startPoint
	public static void aaa(int val){
		for(int counting =0; counting < towerNum; counting++){
			if(towerBuildSequence[counting][val-1] == 1){
				if(towerBuildTime[counting] - baseTowerBuildTime[counting] < towerBuildTime[val-1]){
					towerBuildTime[counting] = towerBuildTime[val-1] + baseTowerBuildTime[counting];
					System.out.println(val + " -> " + (counting+1));
					aaa(counting+1);
					if(towerBuildTime[counting] > result){
						result = towerBuildTime[counting];
					}
				}
			}
		}
	}
}
