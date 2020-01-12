package Baekjoon.tree.Q2250;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q2250_cycho21_Run {

	public static void main(String[] args) {
		Q2250_cycho21_Run main = new Q2250_cycho21_Run();
		main.init();
	}

	private int n;
	private Node[] nodes;
	private int[][] minmax;
	private int seq = 0;
	private int[] index;

	private void init() {
		/*
		 * Get input started..
		 */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			n = Integer.parseInt(br.readLine().trim(), 10);
			nodes = new Node[n + 1];
			index = new int[n + 1];
			for (int i = 0; i <= n; ++i)
				nodes[i] = new Node();
			boolean[] check = new boolean[n];

			for (int i = 0; i < n; ++i) {
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				int vertex = Integer.parseInt(st.nextToken().trim(), 10);
				vertex--;
				int left = Integer.parseInt(st.nextToken().trim(), 10);
				int right = Integer.parseInt(st.nextToken().trim(), 10);
				nodes[vertex].left = left;
				nodes[vertex].right = right;

				if (nodes[vertex].left > 0)
					nodes[vertex].left--;

				if (nodes[vertex].right > 0)
					nodes[vertex].right--;

				if (left != -1)
					check[--left] = true;
				if (right != -1)
					check[--right] = true;
			}

			minmax = new int[10005][2];
			for (int i = 0; i < n; ++i) {
				minmax[i][0] = Integer.MAX_VALUE / 2;
				minmax[i][1] = 0;
			}

			int root = 0;
			for (int i = 0; i < n; ++i)
				if (!check[i])
					root = i;

			solve(root);

		} catch (NumberFormatException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		/*
		 * Get input ended..
		 */
	}

	public void solve(int rootNode) {
		inorderTraversal(rootNode, 0);

		int answer = -1;
		int depth = 1;
		for (int i = 0; i < n; ++i) {
			if (answer < minmax[i][1] - minmax[i][0]) {
				answer = minmax[i][1] - minmax[i][0];
				depth = i;
			}
		}

		System.out.println((depth + 1) + " " + (answer + 1));
	}

	public void inorderTraversal(int idx, int depth) {
		if (nodes[idx].left != -1)
			inorderTraversal(nodes[idx].left, depth + 1);

		if (minmax[depth][0] > seq)
			minmax[depth][0] = seq;
		if (minmax[depth][1] < seq)
			minmax[depth][1] = seq;
		index[idx] = seq++;

		if (nodes[idx].right != -1)
			inorderTraversal(nodes[idx].right, depth + 1);
	}
	
	private class Node {
		public int left;
		public int right;

		public Node() {
			this.left = -1;
			this.right = -1;
		}
	}
}

