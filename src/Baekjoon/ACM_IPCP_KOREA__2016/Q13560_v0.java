package ACM_IPCP_KOREA__2016;


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
    	Arrays.sort(arr); // 승리한 횟수 오른차순으로 저장
    	int sumofwin=0;
    	int sumoflose=0;
    	sumofwin = arr[0]; // 가장 많이 승리한 팀, 0번의 승리한 횟수
    	sumoflose = n-1-arr[n-1]; // 가장 적게 승리한 팀, n-1번의 패배한 횟수
    	
    	for(int i=1;i<n;i++){  		// 1 ~ n-1까지 for문
    		sumofwin+=+arr[i];      // sum of win --> arr[i]까지 승리 횟수를 계속 더함
    		sumoflose+=n-1-arr[n-1-i];      
    		if(sumofwin<(i*(i+1)/2)||sumoflose<(i*(i+1)/2)){
    			System.out.print(-1);   // i번째 까지 승리한 횟수 
    			break;
    			// 승리한 횟수가 왜 i * (i+1)/2의 크기보다 작아야 하는거지..?, 1 --> 3 --> 6 --> 10 ..?
    		}
    		if(i==n-1){
    			System.out.print(1);
    		}
    	}
    }
}

