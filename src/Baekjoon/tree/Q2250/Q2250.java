package tree.Q2250;

import java.util.Scanner;

public class Q2250 {

	public static Tree[] node;
	public static int root = 1; //초기값
	public static int R[];
	public static int L[];
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		node = new Tree[N+1];
		R = new int[N+1];
		L = new int[N+1];
		int n1=0,n2=0,n3=0;
		// Tree 생성
		for(int i=1; i<N+1; i++){
			node[i] = new Tree(i);
		}

		for(int i=1; i<N+1; i++){
			n1 = s.nextInt();
			n2 = s.nextInt();
			n3 = s.nextInt();
			node[n1].value = n1;
			if(n2 != -1){
				node[n1].setLeftChild(node[n2]);
				node[n2].setParent(node[n1]);
			} 
			if(n3 != -1){
				node[n1].setRightChild(node[n3]);
				node[n3].setParent(node[n1]);
			}
		}
		
		// 루트 노드 구하기!
		int check = 1;
		while(check != 0){
			if(node[check].getParent() != null){
				check = node[check].getParent().value;
			}else {
				root = node[check].value;
				check =0;
			}
		}
		
		// node order 및 level 구하기
		aaa(node[root], 1);
		
		
		// 결과값 도출
		for(int i=1; i<N+1; i++){
			if(L[node[i].level] > node[i].order || L[node[i].level] == 0)
				L[node[i].level] = node[i].order;
			if(R[node[i].level] < node[i].order || R[node[i].level] == 0)
				R[node[i].level] = node[i].order;
		}
		
		int result =0, result_level=0;
		for(int i=1; i<N+1; i++){
			if(result < R[i]-L[i]+1){
				result = R[i]-L[i]+1;
				result_level = i;
			}
		}

		System.out.println(result_level);
		System.out.println(result);
		
		s.close();
	}

	public static int order =1;
	public static void aaa(Tree check_node, int level){
		check_node.setLevel(level);
		if(check_node.getLeftChild() != null)
			aaa(check_node.getLeftChild(), level + 1);
		check_node.order = order;
		order++;
		if(check_node.getRightChild() != null)
			aaa(check_node.getRightChild(), level + 1);
	}
}

/*// 출력
System.out.println();
for(int i=1; i<N+1; i++){
	System.out.print(i + "번째  order : " + node[i].order + " level : " + node[i].level);
	if(node[i].getLeftChild() != null)
		System.out.print(" leftChild : " + node[i].getLeftChild().value);
	
	if(node[i].getRightChild() != null)
		System.out.print(" rightChild : " + node[i].getRightChild().value);
	System.out.println();
}

*/


class Tree{
	private Tree Parent = null;
	private Tree LeftChild = null;
	private Tree RightChild = null;
	int value;
	int order;
	int level;
	Tree(int value){
		this.value = value;
	}
	public int getValue() {
        return value;
    }
    public void setValue(int value) {
        this.value = value;
    }
	public Tree getParent() {
		return Parent;
	}
	public void setParent(Tree parent) {
		Parent = parent;
	}
	public Tree getLeftChild() {
		return LeftChild;
	}
	public void setLeftChild(Tree leftChild) {
		LeftChild = leftChild;
	}
	public Tree getRightChild() {
		return RightChild;
	}
	public void setRightChild(Tree rightChild) {
		RightChild = rightChild;
	}
	public int getOrder() {
		return order;
	}
	public void setOrder(int order) {
		this.order = order;
	}
	public void setLevel(int level) {
		this.level = level;
	}
	public int getLevel() {
		return level;
	}
}

