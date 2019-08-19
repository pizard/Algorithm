package tree.Q1967;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q1967 {
	// 트리의 지름
	// 부모노드의 번호   /  자식노드   /  가중치
	
	public static void main(String[] args){
		Q1967 main = new Q1967();
		main.init();
	}
	private List<Edge>[] nodes;
	private boolean[] check;
	private int[] dist;
	private int max_idx=-1;
	private int max_weight=-1;
	
	@SuppressWarnings("unchecked")
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		
		try {
			int n = Integer.parseInt(br.readLine().trim(), 10);
			nodes = (List<Edge>[]) new List[n+1];
			check = new boolean[n+1];
			dist = new int[n+1];
			
			
			for(int i=1; i<n+1; i++){
				nodes[i] = new ArrayList<Edge>();
			}
			
			
			for(int i=0; i<n-1; i++){
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				int n1 = Integer.parseInt(st.nextToken().trim(), 10);
				int n2 = Integer.parseInt(st.nextToken().trim(), 10);
				int weight = Integer.parseInt(st.nextToken().trim(), 10);
				nodes[n1].add(new Edge(n2,weight));
				nodes[n2].add(new Edge(n1,weight));
			}
			
			bfs(1);
			
			Arrays.fill(check,  false);
			Arrays.fill(dist, 0);
			max_weight = -1;
			
			bfs(max_idx);
			

			System.out.println(max_weight);
			
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	void bfs(int startNode){
		Queue<Integer> q = new LinkedList<Integer>();

		q.add(startNode);
		check[startNode] = true;
		dist[startNode] = 0;
		
		while(!q.isEmpty()){
			int x = q.remove();
			for(Edge y : nodes[x]){
				if(check[y.to] == false){
					check[y.to] = true;
					q.add(y.to);
					
					dist[y.to] = dist[x] + y.weight;
					if(max_weight < dist[y.to]){
						max_weight = dist[y.to];
						max_idx = y.to;
					}
				}
			}
		}
	}
	
	private class Edge{
		private int to, weight;
		
		Edge(int to, int weight){
			this.to = to;
			this.weight = weight;
		}
	}
}



