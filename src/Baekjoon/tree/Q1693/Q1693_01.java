package tree.Q1693;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;


public class Q1693_01 {

	// 1,2,3,4... n 번의 색 중 하나의 색으로 칠함
	// 한개의 정점을 색칠할 때마다 1,2,3,4...n의 비용
	// n: 정점의 개수
	// 트리상에 연결된 두 정점
	private List<Edge>[] nodes;
	private int[] value;
	private boolean[] check;
	public static void main(String[] args) {
		Q1693_01 main = new Q1693_01();
		main.init();
	}
	
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try{
			int n = Integer.parseInt(br.readLine().trim(), 10);
			check = new boolean[n+1];
			nodes = (List<Edge>[]) new List[n+1];
			value = new int[n+1];

			for(int i=1; i<n+1; i++){
				nodes[i] = new ArrayList<Edge>();
			}
		
			for(int i=0; i<n-1; i++){
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				int n1 = Integer.parseInt(st.nextToken().trim(), 10);
				int n2 = Integer.parseInt(st.nextToken().trim(), 10);
				nodes[n1].add(new Edge(n2));
				nodes[n2].add(new Edge(n1));
			}

			System.out.println("aa");
			
			
		}catch (Exception e) {
			// TODO: handle exception
		}
	}
	
	private class Edge{
		private int to;
		Edge(int to){
			this.to = to;
		}
	}
	
}
