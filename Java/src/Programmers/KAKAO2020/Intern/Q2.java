package Programmers.KAKAO2020.Intern;

import java.util.ArrayList;

public class Q2 {
    public int[] solution(String s) {
        int[] answer = {};
        String[] temp = s.split("},\\{");
        ArrayList<Integer> resultTemp =  new ArrayList<Integer>();

        for(int i=0; i<temp.length;i++){
            temp[i] = temp[i].replaceAll("\\{", "");
            temp[i] = temp[i].replaceAll("}", "");
        }



        String[][] answerList = new String[temp.length][temp.length];


        for(int i=0; i<temp.length;i++){
            answerList[i] = temp[i].split(",");
        }


        for(int count=1; count <= answerList.length; count++){
            Loop1 : for(int i=0; i<answerList.length; i++){
                if(answerList[i].length == count){
                    for(int j=0; j<answerList.length; j++){
                        if(!resultTemp.contains(Integer.parseInt(answerList[i][j]))){
                            resultTemp.add(Integer.parseInt(answerList[i][j]));
                            continue Loop1;
                        }
                    }
                }
            }
        }

        answer = new int[resultTemp.size()];
        for(int i=0; i<resultTemp.size(); i++){
            answer[i] = resultTemp.get(i);
        }
        return answer;
    }
}
