package Baekjoon.DP.Q2293_COIN;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q2293 {

	
	// N���� ������ ����
	// �� ��ġ�� ���� K���� ����� ��
	// ù���� n�� K
	// ���� n�� ��ġ
	// ����� ���� 2^31���� ����
	
	public static void main(String[] args) {
		Q2293 main = new Q2293();
		main.init();
	}
	
	private int n = 0 ,k = 0, temp = 0;
	private int sort[];
	private int[] D;
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			StringTokenizer st = new StringTokenizer(br.readLine().trim(), " ");
			n = Integer.parseInt(st.nextToken().trim(),10);
			k = Integer.parseInt(st.nextToken().trim(),10);
			D = new int[k];
			D[0] = 1;
			sort = new int[n+1];
			for(int i=1 ; i<n+1; i++){
				sort[i] = Integer.parseInt(br.readLine().trim());
			}
			for(int i=1; i< n+1 ; i++){
				for(int j=i; j<n+1; j++){
					if(sort[i] > sort[j]){
						temp = sort[i];
						sort[i] = sort[j];
						sort[j] = temp;
					}
				}
			}
			for(int i=1; i<=k; i++){
				for(int j=1; j<n+1; j++){
					if(sort[j] <= i && i-j >= 0){
						D[i] += D[i-j];
					}
					else{
						System.out.println(i + "��° �� : " + D[i]);
						break;
					}
				}
			}
			
			System.out.println(D[k]);
			
			
			
			
			
			
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}
