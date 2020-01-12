package Baekjoon.ACM_IPCP_KOREA__2016;


import java.io.*;
import java.util.*;

public class Q13560_v0 {
    public static void main(String[] args)throws Exception{    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	
    	int n=Integer.parseInt(br.readLine().trim());
    	int[] arr=new int[n];
    	StringTokenizer s=new StringTokenizer(br.readLine().trim());
    	for(int i=0;i<n;i++){ 
    		arr[i]=Integer.parseInt(s.nextToken());
    	}
    	Arrays.sort(arr); // �¸��� Ƚ�� ������������ ����
    	int sumofwin=0;
    	int sumoflose=0;
    	sumofwin = arr[0]; // ���� ���� �¸��� ��, 0���� �¸��� Ƚ��
    	sumoflose = n-1-arr[n-1]; // ���� ���� �¸��� ��, n-1���� �й��� Ƚ��
    	
    	for(int i=1;i<n;i++){  		// 1 ~ n-1���� for��
    		sumofwin+=+arr[i];      // sum of win --> arr[i]���� �¸� Ƚ���� ��� ����
    		sumoflose+=n-1-arr[n-1-i];      
    		if(sumofwin<(i*(i+1)/2)||sumoflose<(i*(i+1)/2)){
    			System.out.print(-1);   // i��° ���� �¸��� Ƚ�� 
    			break;
    			// �¸��� Ƚ���� �� i * (i+1)/2�� ũ�⺸�� �۾ƾ� �ϴ°���..?, 1 --> 3 --> 6 --> 10 ..?
    		}
    		if(i==n-1){
    			System.out.print(1);
    		}
    	}
    }
}

