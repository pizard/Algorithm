package Q10828;

import java.util.Scanner;

public class Q10828 {

	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		String command;
		int tail = 0, head = 0, perforInt = -1;
		int[] queue = new int[10001];
		
		for(int i=0;i<N;i++){
			command = scan.next();
			switch(command){
				case "push":
					perforInt = scan.nextInt();
					queue[tail] = perforInt;
					tail++;
					break;
				case "pop":
					if(tail == head){
						System.out.println("-1");
					}else{
						tail--;
						System.out.println(queue[tail]);
						queue[tail] = '\0';						
					}
					break;
				case "size":
					System.out.println(tail - head);
					break;
				case "empty":
					if(tail-head == 0){
						System.out.println("1");
					}else{
						System.out.println("0");						
					}
					break;
				case "top":
					if(tail == head){
						System.out.println("-1");
					}else{
						System.out.println(queue[tail-1]);
					}
					
					break;
			}
			
		}
		scan.close();
	}
}
