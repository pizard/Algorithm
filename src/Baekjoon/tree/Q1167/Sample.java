package tree.Q1167;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;


class Edge{

	public int to;
	public int cost;

	Edge(int to, int cost){
		this.to= to;
		this.cost = cost;
	}
}

public class Sample {

	
	/* 
	 * 트리의 지름
	 * 트레에서 임의의 두 점사이의 거리중 가장 긴 것
	 * 1: 정점의 개수
	 * 2: start Node / end Node / Distance / -1
	 */
	
	public static void main(String[] args) throws IOException{
		Sample m = new Sample();
		m.call();
	}

	int n,m;
	List<Edge>[] g;
	boolean[] check;
	int[] dist;


	void call() throws IOException{

		FastScanner sc = new FastScanner();

		int n = sc.nextInt();
		g = (List<Edge>[]) new List[n+1];
		check = new boolean[n+1];
		dist = new int[n+1];

		for(int i = 1; i <=n; i++){
			int v1 = sc.nextInt();
			int v2;
			
			g[v1] = new ArrayList<Edge>();
			
			while( ( v2 = sc.nextInt() ) != -1 ){

				int w = sc.nextInt();

				g[v1].add(new Edge(v2 ,w));
			}

		}

		bfs(1);
		int max = dist[1];
		int idx = 1;

		for(int i = 2; i<= n; i++){
			if( max < dist[i] ){
				idx = i;
				max = dist[i];
			}
		}
		// System.out.println(idx);

		Arrays.fill(check, false);
		Arrays.fill(dist,0);
		bfs(idx);
		max = dist[1];
		for(int i = 2; i<= n; i++){
			if( max < dist[i] ){
				max = dist[i];
			}
		}
		System.out.println(max);

	}

	void bfs(int start){
		Queue<Integer> q = new LinkedList<Integer>();

		q.add(start);
		check[start] = true;
		dist[start] = 0;

		while(!q.isEmpty()){
			int x = q.remove();

			for( Edge y : g[x]){

				if( check[y.to] == false){
					check[y.to] = true;
					q.add(y.to);

					dist[y.to] = dist[x] + y.cost;
				}
			}
		}
	}
}


class FastScanner {
	BufferedReader br;
	StringTokenizer st;

	public FastScanner(String s) {

		try {

			br = new BufferedReader(new FileReader(s));
		} catch (FileNotFoundException e) {
			throw new RuntimeException(e);
		}
	}

	public FastScanner() {
		br = new BufferedReader(new InputStreamReader(System.in));
	}

	String nextToken() {
		while (st == null || !st.hasMoreElements()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
		return st.nextToken();
	}

	int nextInt() {

		return Integer.parseInt(nextToken());
	}

	long nextLong() {
		return Long.parseLong(nextToken());
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}

	String nextLine() {
		String str = "";
		try {
			str = br.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return str;
	}
}
