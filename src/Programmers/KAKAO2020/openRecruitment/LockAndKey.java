package Programmers.KAKAO2020;

public class LockAndKey {
    // (0,0), (0,1), (0,2) ...
    // (1,0), (1,1), (1,2) ...
    // (2,0), (2,1), (2,2) ...
    // [0, 0, 0] 000
    // [1, 0, 0] 001
    // [0, 1, 1] 001

    public boolean solution(int[][] key, int[][] lock) {
        boolean answer = false;
        int size = key.length;
        int[][] temp = new int[size][size];

        // 회전
        LOOP1 : for(int i=0; i<4; i++){
            key = rotateClockwise90(key, 0);
            if(solveLock2(temp, lock, size, size)){
                answer = true;
            }

        }

        return answer;
    }

    // M과 N이 다른 경우에 대한 부분 곤리
    public boolean solveLock2(int[][] key, int[][] lock, int keySize, int lockSize){
        boolean result = false;
        Loop1 : for(int i=0; i<keySize; i++){
            for(int j=0; j<keySize; j++){
//                Loop2 : for(int m=0; m < size; m++) {
//                    for (int n = 0; n < size; n++) {
//                        if(validation(key, i+m-size, 1) && validation(key, j+n-size, 1)){
//                            if( (key[i][j] + lock[i+m-size][j+n-size]) != 1){
//                                continue Loop2;
//                            }
//                        }
//                    }
//                    result = true;
//                }

            }
        }

        return result;
    }
    // 회전
    public int[][] rotateClockwise90(int[][] key, int Anti){
        int [][] result = new int [key.length][key[0].length];
        for(int i=0; i < key.length;i++) {
            for (int j = 0; j < key[i].length; j++) {
                // 정방향
                if(Anti == 0){
                    result[i][j] = key[key.length-1-j][i];
                }else{
                    result[i][j] = key[j][key.length-1-i];
                }
            }
        }


        return result;
    }


    // 회전, direction 0: up, 1: left, 2: down, 3: right
    public int[][] moveKey(int[][] key, int direction, int distance){
        int [][] result = new int [key.length][key[0].length];
        // up & down
        if(direction%2 == 0){
            // distance : + -> down, - -> up
            if(direction == 0){
                distance = -distance;
            }
            for(int i=0; i < key.length;i++){
                for(int j=0; j < key[i].length;j++){
                    if(validation(key, i+distance, 1)){
                        result[i+distance][j] = key[i][j];
                    }
                }
            }
        }
        // left & right
        else{
            // distance : + -> right, - -> left
            if(direction == 1){
                distance = -distance;
            }
            for(int i=0; i<key.length;i++){
                for(int j=0; j<key[i].length;j++){
                    if(validation(key, i+distance, 2)){
                        result[j][i+distance] = key[j][i];
                    }
                }
            }
        }
        return result;
    }



    public boolean validation(int[][] temp, int value, int dimension){
        if(dimension == 1){
            if(0 <= value && value < temp.length){
                return true;
            }
        }else{
            if(0 <= value && value < temp[0].length){
                return true;
            }
        }
        return false;
    }

    public void printArray(int[][] key){
        for(int i=0; i<key.length; i++){
            for(int j=0; j<key.length; j++){
                System.out.print(key[i][j] + " ");
            }
            System.out.println();
        }
    }

}
