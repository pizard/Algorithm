package Programmers.KAKAO2020;

// 문자열 압출 : https://programmers.co.kr/learn/courses/30/lessons/60057

public class StringCompression {

    public static int solution(String s) {
        int answer = 0;
        int wordLoc = 0;
        int wordCount = 0;

        String resultWord = s;
        String tempResultWord = "";
        String tempWord = "";


        for(int i=1; i <= (s.length())/2; i++){
            wordLoc = 0;
            tempResultWord = "";
            wordCount = 0;

            while(wordLoc < s.length()){
                if(s.length() >= (wordLoc+i)){
                    // 마지막인 경우 : input * 2
                    if(s.length()  == (wordLoc + i)){
                        // 같은 경우
                        if(tempWord.equals(s.substring(wordLoc, wordLoc+i))){
                            wordCount++;
                            tempResultWord += wordCount + tempWord;
                        // 다른 경우
                        } else {
                            if(wordCount != 1){
                                tempResultWord += wordCount + tempWord;
                            } else{
                                tempResultWord += tempWord;
                            }
                            tempResultWord += s.substring(wordLoc, wordLoc + i);
                        }
                    }
                    // 이전과 같은 경우 & 첫번째인 경우 : pass
                    else if( tempWord.equals(s.substring(wordLoc, wordLoc+i))
                                || wordLoc == 0) {
                        wordCount++;
                    }
                    // 이전과 다른 경우 : input
                    else {
                        if(wordCount != 1){
                            tempResultWord += wordCount + tempWord;
                        } else{
                            tempResultWord += tempWord;
                        }
                        wordCount = 0;

                    }
                    wordCount++;
                    tempWord = s.substring(wordLoc, wordLoc+i);
                    System.out.println(tempWord);
                }else{  // 마지막 case
                    tempResultWord = tempResultWord + s.substring(wordLoc, s.length());
                    System.out.println(s.substring(wordLoc, s.length()));
                }
                wordLoc += i;
            }
            if(resultWord.length() > tempResultWord.length()){
                resultWord = tempResultWord;
            }
            System.out.println("------------- " + "tempNum : " + i + " temp Result : "  + tempResultWord + " -------------");
        }
        System.out.println("result : "  + resultWord);



        return answer;
    }
}
