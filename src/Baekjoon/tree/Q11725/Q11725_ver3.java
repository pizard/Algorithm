package tree.Q11725;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q11725_ver3 {

	public static void main(String[] args) {
		Q11725_ver3 main = new Q11725_ver3();
		main.init();
	}
	
	private List<Node>[] nodes;
	private Node[] result;
	private boolean[] check;
	
	@SuppressWarnings("unchecked")
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		try{
			int n = Integer.parseInt(br.readLine().trim(), 10);
			nodes = (List<Node>[]) new List[n+1];
			result = new Node[n+1];
			check = new boolean[n+1];
			
			
			for(int i=1; i<n+1; i++){		// 1 ~ n
				nodes[i] = new ArrayList<Node>();
				result[i] = new Node(-1);
			}

			int n1, n2;
			for(int i=0; i<n-1; i++){		// n-1회 반복
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				n1 = Integer.parseInt(st.nextToken().trim(), 10);
				n2 = Integer.parseInt(st.nextToken().trim(), 10);
				nodes[n1].add(new Node(n2));	// n1이라는 nodes arrayList에 n2라는 Node를 넣음
				nodes[n2].add(new Node(n1));	// 반대로 적용
			}
			
			arrangement(1);
			
			for(int i=2; i<=n;i++)
				System.out.println(result[i].n1);

		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	private void arrangement(int n){
		Queue<Integer> q = new LinkedList<Integer>();

		q.add(n);
		check[n] = true;
			
		// 1
		// > 2,3,4,5
		// 2 > 1
		
		// result[a].n1,   a: parent  /  n1: child
		
		while(!q.isEmpty()){
			int x = q.remove();
			for(Node y : nodes[x]){
				if(check[y.n1] == false){
					check[y.n1] = true;
					q.add(y.n1);
					result[y.n1].setN1(x);
					
				}
			}
			
		}
		
	}
	
	
	private class Node{
		int n1;
		
		Node(int n1){
			this.n1 = n1;
		}

		public void setN1(int n1) {
			this.n1 = n1;
		}
		public int getN1() {
			return n1;
		}
	}
	
	
}
