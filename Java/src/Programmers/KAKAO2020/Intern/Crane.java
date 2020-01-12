package Programmers.KAKAO2020.Intern;

import java.util.ArrayList;
import java.util.Stack;


// [1,5,3,5,1,2,1,4]
public class Crane {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;

        Stack<Integer> popArray = new Stack<>();
        ArrayList<Stack<Integer>> stack= new ArrayList<>();
        Stack<Integer> temp = new Stack<Integer>();


        for(int i=0; i<board.length; i++){
            temp = new Stack<Integer>();
            for(int j=board[0].length-1; j>=0; j--){
                if(board[j][i] != 0){
                    temp.push(board[j][i]);
                }
            }
            stack.add(temp);
        }
        // {0,0,0,0,0}
        // {0,0,1,0,3}
        // {0,2,5,0,1}
        // {4,2,4,4,2}
        // {3,5,1,3,1}

        // {1,5,3,5,1,2,1,4};
        //  4 3 1 1 3 2 x 4

        for(int i=0; i<moves.length; i++){
            // stack이 비어있지 않은 경우
            if(!stack.get(moves[i]-1).empty()) {
                if(!popArray.empty()){
                    if (popArray.peek() == stack.get(moves[i] - 1).peek()) {
                        popArray.pop();
                        stack.get(moves[i] - 1).pop();
                        answer += 2;
                    } else {
                        popArray.push(stack.get(moves[i] - 1).peek());
                        stack.get(moves[i] - 1).pop();
                    }
                }else {
                    popArray.push(stack.get(moves[i] - 1).peek());
                    stack.get(moves[i] - 1).pop();
                }
            }
        }
        return answer;
    }
}
