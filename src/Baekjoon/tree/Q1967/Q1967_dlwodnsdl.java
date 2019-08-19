package tree.Q1967;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q1967_dlwodnsdl {

	public static void main(String[] args)throws Exception{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	int n=Integer.parseInt(br.readLine().trim());
    	StringTokenizer s;
    	int max=0;
    	Queue<Node> queue=new LinkedList<Node>();
    	Node[] arr=new Node[n+1];
    	for(int i=1;i<=n;i++){
    		arr[i]=new Node();
    	}
    	for(int i=1;i<n;i++){
    		s=new StringTokenizer(br.readLine().trim());
    		int u=Integer.parseInt(s.nextToken());
    		int v=Integer.parseInt(s.nextToken());
    		int w=Integer.parseInt(s.nextToken());
    		arr[v].distance=w;
    		arr[v].parent=arr[u];    				
    		arr[u].numofsons++;
    	}
    	for(int i=1;i<=n;i++){
    		if(arr[i].numofsons==0){
    			queue.add(arr[i]);
    		}
    	}
    	while(!queue.isEmpty()){
    		Node son=queue.poll();
    		if(son.maxsum>max){
    			max=son.maxsum;
    		}
    		Node parent=son.parent;
    		if(parent!=null){
    			parent.maxsum=Math.max(parent.maxsum, parent.max+son.max+son.distance);
        		parent.max=Math.max(parent.max,son.max+son.distance);
        		if(--parent.numofsons==0){
        			queue.add(parent);
        		}
    		}    		
    	}
    	System.out.print(max);
    	
    }
	
}

class Node{
	Node parent;
	int distance;
	int max;
	int maxsum;
	int numofsons;
	public Node(){
		this.max=0;
		this.numofsons=0;
		this.distance=0;
		this.maxsum=0;
	}
}