package realization.Q2490;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q2490 {

	public static void main(String[] args) {
		Q2490 main = new Q2490();
		main.init();
	}
	private int[][] yut = new int[3][4];
	private int[] result = new int [3];
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			for(int i=0; i<3; i++){
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				yut[i][0] = Integer.parseInt(st.nextToken());
				yut[i][1] = Integer.parseInt(st.nextToken());
				yut[i][2] = Integer.parseInt(st.nextToken());
				yut[i][3] = Integer.parseInt(st.nextToken());
				if(yut[i][0] == 0)
					result[i]++;
				if(yut[i][1] == 0)
					result[i]++;
				if(yut[i][2] == 0)
					result[i]++;
				if(yut[i][3] == 0)
					result[i]++;
				switch(result[i]){
					case 0:
						System.out.println("E");	// 윷 - 배 4    1 1 1 1  D
						break;
					case 1:
						System.out.println("A");	// 도 - 배 1 등 3 0 1 1 1  A
						break;
					case 2:
						System.out.println("B");	// 개 - 배 2 등 2 0 0 1 1  B
						break;
					case 3:
						System.out.println("C");	// 걸 - 배 3 등 1 0 0 0 1  C
						break;
					case 4:
						System.out.println("D");	// 모 - 등 4    0 0 0 0  E
						break;
					default:
						break;
				}
			}
			
			
			
			
			

		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}
