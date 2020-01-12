package Baekjoon.tree.Q2250;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q2250_ver2 {

	
	public static void main(String[] args){
		Q2250_ver2 main = new Q2250_ver2();
		main.init();
	}
	
	private int N;
	private node_2[] nodes;
	private int[][] minmax;
	private int seq = 1;
	private int[] index;
	
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try{
			N = Integer.parseInt(br.readLine().trim());
			nodes = new node_2[N+1];
			index = new int[N+1];
			int vertex, left, right;
			for(int i=1; i < N+1; i++){
				nodes[i] = new node_2();
			}
			boolean[] check = new boolean[N+1];
			
			for(int i=0; i < N; i++){
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				vertex = Integer.parseInt(st.nextToken().trim());
				left = Integer.parseInt(st.nextToken().trim());
				right = Integer.parseInt(st.nextToken().trim());
				nodes[vertex].left = left;
				nodes[vertex].right = right;
				
				if(left != -1)
					check[left] = true;
				if(right != -1)
					check[right] = true;
			}
			
			minmax = new int[N+1][2];
			for(int i=1; i < N+1 ; i++){
				minmax[i][0]= N+1;
				minmax[i][1] = 0;
			}
			
			
			int root = 0;
			for(int i=1; i < N+1 ; i++){
				if(!check[i])
					root = i;
			}
			
			solve(root);
			
		}catch(IOException e){
			e.printStackTrace();
		}
	}
	
	public void solve(int rootNode){
		inorderTraversal(rootNode, 1);
		
		int answer = -1;
		int depth = -1;
		for(int i=0; i<N+1; i++){
			if(answer < minmax[i][1] - minmax[i][0]){
				answer = minmax[i][1] - minmax[i][0];
				depth = i;				
			}
		}
		System.out.println(depth + " " + (answer+1) );
			
		
	}
	
	public void inorderTraversal(int idx, int depth){
		if(nodes[idx].left != -1)
			inorderTraversal(nodes[idx].left, depth + 1);
		
		if(minmax[depth][0] > seq)
			minmax[depth][0] = seq;
		if(minmax[depth][1] < seq)
			minmax[depth][1] = seq;
		seq++;
		
		if(nodes[idx].right != -1)
			inorderTraversal(nodes[idx].right, depth + 1);
	}
	
}

class node_2 {
	public int parent;
	public int left;
	public int right;
	
	public node_2() {
		this.left = -1;
		this.right = -1;
		this.parent = -1;
	}
	
}
