package Programmers.Hash;

import java.util.*;

// 베스트 앨범 : https://programmers.co.kr/learn/courses/30/lessons/42579
public class BestAlbem {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genresOrder =  new HashMap<String, Integer>();
        for(int i=0; i<genres.length; i++){
            if(genresOrder.containsKey(genres[i])){
                genresOrder.put(genres[i], genresOrder.get(genres[i]) + plays[i]);
            }else{
               genresOrder.put(genres[i], plays[i]);
            }
        }
        genresOrder = sortByValue(genresOrder, 1);

        int count = 0;
        int[] answer = new int[genresOrder.size()*2];


        ArrayList<Integer> answerList = new ArrayList<Integer>();
        for(String genre : genresOrder.keySet()){
            int[] firstSong = new int[2];  // 0: play count, 1: song Number
            int[] secondSong = new int[2]; // 0: play count, 1: song Number
            for(int i=0; i<genres.length; i++){
                if(genre.equals(genres[i])){
                    if(plays[i] > firstSong[0]){
                        secondSong[0] = firstSong[0];
                        secondSong[1] = firstSong[1];
                        firstSong[0] = plays[i];
                        firstSong[1] = i;
                    }else if(plays[i] > secondSong[0]){
                        secondSong[0] = plays[i];
                        secondSong[1] = i;
                    }
                }
            }

            answerList.add(firstSong[1]);
            count++;
//            System.out.println(firstSong[1]);
            if(secondSong[0] != 0){
                answerList.add(secondSong[1]);
                count++;
//                System.out.println(secondSong[1]);
            }
            answer = new int[answerList.size()];
            for(int i=0; i<answerList.size(); i++){
                answer[i] = answerList.get(i);
            }
        }
        return answer;
    }

    // num  0: ascending, 1: descending
    public static <K, V extends Comparable<? super V>> Map<K, V> sortByValue(Map<K, V> map, int num) {
        List<Map.Entry<K, V>> list = new ArrayList<>(map.entrySet());
        if(num == 0)
            list.sort(Map.Entry.comparingByValue());
        else
            list.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        Map<K, V> result = new LinkedHashMap<>();
        for (Map.Entry<K, V> entry : list) {
            result.put(entry.getKey(), entry.getValue());
        }

        return result;
    }
}
