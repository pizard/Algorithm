package Programmers.Hash;

import java.util.HashMap;

// 위장 : https://programmers.co.kr/learn/courses/30/lessons/42578?language=java
public class Camouflage {

    public int Camouflage(String[][] clothes) {
        int answer = 0;

        clothes = new String[][]{{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        HashMap clothesNum = new HashMap();

        for(String[] clothType : clothes){
            if(clothesNum.containsKey(clothType[1])){
                int tempNum = (int) clothesNum.get(clothType[1])+1;
                clothesNum.put(clothType[1], tempNum);
            }else{
                clothesNum.put(clothType[1], 1);
            }
        }
        for(Object temp : clothesNum.values()){
            if(answer  ==  0){
                answer = (int) temp + 1;
            }else{
                answer =  answer * ((int) temp + 1);
            }
        }
        answer--; // 어떤 옷도 입고 있지 않은 경우
        return answer;
    }

    public int Camouflage() {
        return  Camouflage(null);
    }
}
