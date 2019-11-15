package Programmers.KAKAO2020;

public class StringCompression2 {
    public static int solution(String s) {
        int answer = 0;
        int wordLoc = 0;
        int wordCount = 0;

        String resultWord = s;
        String tempResultWord = "";

        String tempWord = "";           // 현재 단어
        String tempForwardWord = "";    // 이전 단어

        for(int i=1; i <= (s.length())/2; i++){
            wordLoc = 0;
            tempResultWord = "";
            wordCount = 1;

            while(wordLoc < s.length()){
                // case
                if(s.length() >= (wordLoc+i)){
                    tempWord = s.substring(wordLoc, wordLoc+i);
                    // System.out.println(tempWord);

                    // 첫 단어인 경우
                    if(wordLoc == 0){
                        wordCount = 1;
                    }
                    // 마지막인 경우
                    else if(s.length() == (wordLoc+i) || s.length() < (wordLoc+i+i)){
                        if(tempForwardWord.equals(tempWord)){
                            // 같은 경우
                            wordCount++;
                            tempResultWord += wordCount + tempForwardWord;
                        }else{
                            // 다른 경우
                            if(wordCount != 1) {
                                tempResultWord += wordCount + tempForwardWord;
                            } else{
                                tempResultWord += tempForwardWord;
                            }
                            tempResultWord += tempWord;
                        }
                    }
                    // 같은 경우
                    else if(tempForwardWord.equals(tempWord)){
                        wordCount++;
                    }
                    // 다른 경우
                    else{
                        if(wordCount != 1) {
                            tempResultWord += wordCount + tempForwardWord;
                        } else{
                            tempResultWord += tempForwardWord;
                        }
                        wordCount = 1;
                    }

                    tempForwardWord = tempWord;
                }
                // 나머지 자투리 처리
                else{
                    tempResultWord = tempResultWord + s.substring(wordLoc, s.length());
                    // System.out.println(s.substring(wordLoc, s.length()));
                }
                wordLoc += i;
            }
            if(resultWord.length() > tempResultWord.length()){
                resultWord = tempResultWord;
                // System.out.println(" ------------- tempResult : "  + resultWord + " -------------");
            }
        }
        answer = resultWord.length();

        return answer;
    }
}