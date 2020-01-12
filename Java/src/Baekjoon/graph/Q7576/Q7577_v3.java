package Baekjoon.graph.Q7576;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q7577_v3 {

	public static void main(String[] args) {
		Q7577_v3 main = new Q7577_v3();
		main.init();
	}
	private int[][] tomato;
	private boolean[][] check;
	private int X;
	private int Y;
	int result;
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			StringTokenizer xy = new StringTokenizer(br.readLine(), " ");
			Y = Integer.parseInt(xy.nextToken().trim()); // 6
			X = Integer.parseInt(xy.nextToken().trim()); // 4
			tomato = new int [X+1][Y+1];
			check = new boolean [X+1][Y+1];
				
			for(int i=1; i<X+1; i++){
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				for(int j=1; j<Y+1; j++){
					tomato[i][j] = Integer.parseInt(st.nextToken().trim());
				}
			}
			Queue q = new LinkedList();
			
			for(int i=1; i<X+1; i++){
				for(int j=1; j<Y+1; j++){
					
				}
			}
			
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	
	private void solve(int x, int y, int count){
		if((0<x && x<X) && (0<y&&y<Y) && (check[x][y] != true)){
			// ����
			// x-1 x+1
			// y-1 y+1
			tomato[x][y] = 1;
			check[x][y] = true;
			count = count + 1;
			if(result < count){
				result = count;
			}
			if(x+1<X)
				if(check[x+1][y] != true)
					solve(x+1,y, count);
			
			if(x-1>=1)
				if(check[x-1][y] != true)
					solve(x-1,y, count);
			
			if(y+1<X)
				if(check[x][y+1] != true)
					solve(x,y+1, count);
			
			if(y-1>=1)
				if(check[x][y-1] != true)
					solve(x,y-1, count);
			
		}
	}
}
