package Baekjoon.tree.Q1991;

import java.util.Scanner;

public class Q1991 {
	private class TreeNode{
		char data;
		TreeNode left;
		TreeNode right;
		
		public TreeNode(char data){
			this.data = data;
			this.left = null;
			this.right = null;
		}
		public char getData(){
			return this.data;
		}
	}
	
	public class LinkedTree{
		private TreeNode root;
		
		public TreeNode makeBT(TreeNode bt1, char data, TreeNode bt2){
			TreeNode root = new TreeNode(data);
			root.left = bt1;
			root.right = bt2;
			return root;
		}
		
		public void preorder(TreeNode root){
			System.out.print(root.data + " ");
			preorder(root.left);
			preorder(root.right);
		}
	}
	
	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		TreeNode[] node = new TreeNode [10];
		
		char ppp = '0';
		for(int i=0; i<N; i++){
			System.out.println("-------------------------");
		}
		// ������ȸ
		for(int i=0; i<N; i++){

		}
	}
	
}
