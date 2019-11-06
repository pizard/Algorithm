package Programmers.Hash;

import java.util.HashMap;

public class Camouflage_type2 {

    public int Camouflage(String[][] clothes) {
        int answer = 1;

        clothes = new String[][]{{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        HashMap<String, Integer> map = new HashMap();

        for(int i=0; i<clothes.length; i++){
            String key = clothes[i][1];
            if(map.containsKey(key)){
                map.put(key, map.get(key)+1);
            }else{
                map.put(key, 1);
            }
        }

        for(int temp : map.values()){
            answer = answer * (temp + 1);
        }
        answer--;
        return answer;
    }
}
