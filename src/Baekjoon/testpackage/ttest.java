package Baekjoon.testpackage;


public class ttest {
	public static void main(String[] args) {
	
		String q = null;
		if(q == null){
			System.out.println("111");
		}
		
		Tree[] node = new Tree[2];
		node[0] = new Tree(10);
		node[1] = new Tree(11);
		System.out.println("진행 잘 되는중~");
		
		
		node[0].setParent(node[1]);
		
		if(node[0].getParent() == null)
			System.out.println("0번 노드의 부모는 NULL입니다.");
		
		if(node[0].getParent() != null)
			System.out.println("0번 노드의 부모는 NULL이 아닙니다.");

		if(node[1].getParent() == null)
			System.out.println("1번 노드의 부모는 NULL입니다.");
		
		if(node[1].getParent() != null)
			System.out.println("1번 노드의 부모는 NULL이 아닙니다.");

		
		System.out.println("마무리~");
		
/*		if(node[0].getParent() == null)
			System.out.println("1번의 부모노드는 NULL입니다.");*/
			
		
	}
}

class Tree{
	private Tree Parent;
	private Tree LeftChild;
	private Tree RightChild;
	int value;
	int count;
	Tree(int value){
		this.value = value;
	}
	
    public void setValue(int value) {
        this.value = value;
    }
    public int getValue() {
        return value;
    }

	public Tree getParent() {
		return Parent;
	}
	public void setParent(Tree parent) {
		this.Parent = parent;
	}
	public Tree getLeftChild() {
		return LeftChild;
	}
	public void setLeftChild(Tree leftChild) {
		this.LeftChild = leftChild;
	}
	public Tree getRightChild() {
		return RightChild;
	}
	public void setRightChild(Tree rightChild) {
		this.RightChild = rightChild;
	}
	public int getCount() {
		return count;
	}
	public void setCount(int count) {
		this.count = count;
	}
}
