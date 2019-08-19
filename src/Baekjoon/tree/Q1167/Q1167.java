package tree.Q1167;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

import tree.Q11725.Q11725_ver2.TreeNode;

public class Q1167 {

	
	/* 
	 * 트리의 지름
	 * 트레에서 임의의 두 점사이의 거리중 가장 긴 것
	 * 1: 정점의 개수
	 * 2: start Node / end Node / Distance / -1
	 */	
	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		
		int V = scan.nextInt();
		int check;
		
		for(int i =0; i<V; i++){
			do{
				check = scan.nextInt();
				if(check != -1){
					
				}
			}while(check != -1);
			
			
		}
	}
	
	public class TreeNode<T> implements Iterable<TreeNode<T>>{
	    private T data;
	    private TreeNode<T> parent;
	    private List<TreeNode<T>> children;
	 
	    public TreeNode(T data) {
	        this.data = data;
	        this.children = new LinkedList<TreeNode<T>>();
	    }
	 
	    public TreeNode<T> addChild(T child) {
	        TreeNode<T> childNode = new TreeNode<T>(child);
	        childNode.parent = this;
	        this.children.add(childNode);
	        return childNode;
	    }
	 
	    @Override
	    public Iterator<TreeNode<T>> iterator() {
	        // TODO Auto-generated method stub
	        return null;
	    }
	}
}
