package Programmers.Greedy;

public class GymCloth {
    public static void main(String[] args){
        int n =5;
        int[] lost = new int[]{2,4};
        int[] reserve = new int[]{1,3,5};
        int answer = n-lost.length;
        
        for(int i=0; i<lost.length; i++) {
        	for(int j=0; j<reserve.length; j++) {
                if(lost[i] == reserve[j]){
                    lost[i] = -1;
                    reserve[j] = -3;
                    answer++;
                }
        	}
        }
        
        lost = Sorting(lost);
        reserve = Sorting(reserve);
        

        for(int lostValue : lost){
            for(int i=0; i<reserve.length; i++){
                if(lostValue == reserve[i]){
                    answer++;
                    // k++;
                    reserve[i] = -1;
                    break;
                }else if(lostValue-1 == reserve[i]){
                    answer++;
                    // k++;
                    reserve[i] = -1;
                    break;
                }else if(lostValue+1 == reserve[i]){
                    answer++;
                    // k++;
                    reserve[i] = -1;
                    break;
                }
            }
        }
        
    	System.out.println(answer);
    }
    
    
    public static int[] Sorting(int[] intList) {
    	
    	for(int i=0; i < intList.length-1;i++) {
    		for(int j=0; j < intList.length-1; j++) { 
    			if(intList[j] > intList[j+1]) {
    				int temp = intList[j];
    				intList[j] = intList[j+1];
    				intList[j+1] = temp;
    			}
    		}
    	}
    	return intList;
    }

    
}