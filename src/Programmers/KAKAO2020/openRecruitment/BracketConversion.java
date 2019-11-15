package Programmers.KAKAO2020;

import java.util.Stack;

public class BracketConversion {
    public String solution(String p) {

        String answer = "";
        String[] splitList =  new String[2]; // 0: u, 1: v

        //  1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        if("".equals(p)){
            return "";
        }else{
            //  2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
            splitList = splitWord(p);

            //  3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
            if(checkCompleteWord(splitList[0])) {
                answer += splitList[0];
                //  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
                answer += solution(splitList[1]);
            }
            //  4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
            else{
                answer += notCorrectWord(splitList[0], splitList[1]);
            }
        }

        return answer;
    }


    public String[] splitWord(String word){
        String[] splitList =  new String[2]; // 0: u, 1: v
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<word.length(); i++){
            if(word.charAt(0) == word.charAt(i)){
                stack.push(word.charAt(0));
            }else{
                stack.pop();
                if(stack.empty()){
                    splitList[0] = word.substring(0, i+1);
                    splitList[1] = word.substring(i+1, word.length());
                    break;
                }
            }

        }
        return  splitList;
    }

    public boolean checkCompleteWord(String word){
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<word.length(); i++){
            if('(' == word.charAt(i)){
                stack.push(word.charAt(0));
            } else {
                if(stack.empty()){
                    return false;
                }
                stack.pop();
            }
        }
        return true;
    }

    //  4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    public String notCorrectWord(String wordU, String wordV){
        String result = "";

        //  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        result += "(";

        //  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        result += solution(wordV);


        //  4-3. ')'를 다시 붙입니다.
        result += ")";
        //  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        for(int i=1; i<wordU.length()-1; i++){
            if('(' == wordU.charAt(i)){
                result += ")";
            } else {
                result += "(";
            }
        }

        //  4-5. 생성된 문자열을 반환합니다.
        return result;
    }
}