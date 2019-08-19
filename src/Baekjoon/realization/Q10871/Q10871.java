package realization.Q10871;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q10871 {

	public static void main(String[] args) {
		Q10871 main = new Q10871();
		main.init();
	}
	private int[] array;
	
	private void init(){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken().trim());
			int X = Integer.parseInt(st.nextToken().trim());
			array = new int[N];
			StringTokenizer st_array = new StringTokenizer(br.readLine(), " ");
			for(int i=0; i<N; i++){
				array[i] = Integer.parseInt(st_array.nextToken().trim());
			}
			for(int i=0; i<N; i++){
				if(array[i] < X)
					System.out.print(array[i] + " ");
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
