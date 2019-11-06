package Programmers.StackQueue;


import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

// 프린터 : https://programmers.co.kr/learn/courses/30/lessons/42587
public class Printer {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        ArrayList<Integer> order = new ArrayList<Integer>();
        for(int temp : priorities){
//            if(!order.contains(temp)){
            order.add(temp);
//            }
        }


        Collections.sort(order, Collections.reverseOrder());
        Queue<Integer> queue = new LinkedList<Integer>();
        Queue<Integer> queue2 = new LinkedList<Integer>();
        for(int i=0; i<priorities.length;i++){
            queue.add(priorities[i]);
            queue2.add(i);
        }

        Loop1 : while(true){
            Loop2 : for(int temp : order){
                while(queue.element() != null){
                    if(temp == queue.element()){
                        if(queue2.element() == location){
                            answer++;
                            break Loop1;
                        }
                        answer++;
                        queue.poll();
                        queue2.poll();
                        continue Loop2;
                    }else{
                        queue.add(queue.poll());
                        queue2.add(queue2.poll());
                    }
                }

            }
        }
        return answer;
    }
}
