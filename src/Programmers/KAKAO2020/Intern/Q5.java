package Programmers.KAKAO2020.Intern;

import java.util.Stack;

public class Q5 {
    public int solution(int[] stones, int k) {
        int answer = 200000000;
        double length = 200000000;

        int bottom = 0;
        int top = 200000000;

        int count = 3;
        LOOP1 : while(length >= 1){


            for(int i=0; i<stones.length;i++){
                if(stones[i] >= answer){
                    count = 3;
                } else{
                    if(count == 0){
                        bottom = (bottom + top)/2;
                        continue LOOP1;
                    }else{
                        count--;
                    }
                }
            }
            answer += length;

            if(length == 1){
                length = 0;
            }
        }

        return answer;
    }
}