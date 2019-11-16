package Running;


import Programmers.KAKAO2020.Intern.Q5;
import Utils.Matrix;

public class Default {
    public static void main(String[] args){



        int[][] key  = {{0, 0, 0}, {1, 0, 0}, {0, 1, 1}};
        int[][] lock = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};

//        LockAndKey lockAndKey = new LockAndKey();
//        System.out.println(lockAndKey.solution(key, lock));









//        Q4 question = new Q4();
//        System.out.println(question.solution(k, room_number));


//        String[] user_id =  {"frodo", "fradi", "crodo", "abc123", "frodoc"};
//        String[] banned_id = {"*rodo", "*rodo", "******"};
//        Q3 question = new Q3();
//        System.out.println(question.solution(user_id, banned_id));


//        int[] stones = {2, 4, 5, 3, 2, 1, 4, 2, 5, 1};
//        int k = 3;
//        Q5 question = new Q5();
//        System.out.println(question.solution(stones, k));

        Matrix a = new Matrix();

        System.out.println(
                a.productMatrix2D(a.productMatrix2D(a.makeMatrix2D("[9.25, 0.75]"), a.makeMatrix2D("[[0.32, 0.16],[0.64, 0.12]]")), a.makeMatrix2D("[3.25],[6.75]"))[0][0]
        );
    }
}
