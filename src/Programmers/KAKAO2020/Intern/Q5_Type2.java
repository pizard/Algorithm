package Programmers.KAKAO2020.Intern;

public class Q5 {
    public int solution(int[] stones, int k) {
        int answer = 0;
        int location = -1;
        int prevLocation = -1;
        boolean stop = true;
        while(stop){
            for(int i=location+1; i <= location+k; i++){
                if(i == stones.length){ // 마지막 위치인 경우
                    location = -1;
                    answer++;
                    break;
                }else{ // moving
                    if(stones[i] > 0){
                        location = i;
                        stones[i]--;
                        break;
                    }
                }
            }
            // not Moving
            if(prevLocation == location){
                stop = false;
            }
            prevLocation = location;

        }

        return answer;
    }
}
