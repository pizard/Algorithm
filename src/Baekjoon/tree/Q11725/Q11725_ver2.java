package tree.Q11725;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;


public class Q11725_ver2 {
	
//	public class TreeNode{
//	TreeNode parent;
//	String data;
//	ArrayList <TreeNode> Children;
//}	
//
//public void printTree(TreeNode root){
//	System.out.println(root.data);for(int i=0;i < root.Children.size(); i++){
//		printTree(root.Children.get(i));
//	}
//}
	
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
	
	public static void main(String[] args){
		
		
	}
	
	
	
	
	
	
}
