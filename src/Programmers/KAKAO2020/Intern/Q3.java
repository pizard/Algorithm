package Programmers.KAKAO2020.Intern;

import java.util.regex.Pattern;

public class Q3 {
    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;

        for(int i=0; i<banned_id.length; i++){

            banned_id[i] = "^" + banned_id[i].replaceAll("\\*", "\\\\w") + "$";
        }

        for(int i=0; i<user_id.length; i++){
            for(int j=0; j<banned_id.length; j++){
                if(Pattern.matches(user_id[i], banned_id[j])){
                    System.out.println("user_id : " + user_id[i]);
                    System.out.println("banned_id : " + banned_id[j]);
                }
            }
        }

        return answer;
    }
}
