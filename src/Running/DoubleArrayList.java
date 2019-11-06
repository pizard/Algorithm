package Running;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;


// ㅁ_ㅁ
public class DoubleArrayList {


    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);


        String[][] clothes = new String[100][100]; // 0 : type, 1 ~

        while(scan.hasNext()){
            String tempName = scan.next();
            String tempType = scan.next();

            if(checkContain(clothes, tempType)){
                // clothes[getFirstNullLocation(clothes, 2)] = tempType;
            }else{

            }

        }
    // [[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]
    }

    public static boolean checkContain(String[][] clothes, String tempType){
        for(String[] type : clothes){
            if(clothes.equals(type)){
                return true;
            }
        }
        return false;
    }

    public static int getFirstNullLocation(String[][] clothes, int dimension, int dimensionLocation){
        int result =0;
        if(dimension == 1){
            for(int i=0; i<clothes.length;i++){
                if(clothes[i] == null){
                    result = i;
                    break;
                }
            }
            result--; // for get lastValueLocation Not firstNullLocation
        }else if(dimension == 2){
            for(int i=0; i<clothes[dimensionLocation].length;i++){
                if(clothes[dimensionLocation][i] == null){
                    result = i;
                    break;
                }
            }
            result--; // for get lastValueLocation Not firstNullLocation
        }else{
            System.out.println("dimension을 1 혹은 2를 입력해주세요.");
        }
        return result;
    }

    public static int getFirstNullLocation(String[][] clothes, int dimension) {
        return getFirstNullLocation(clothes, dimension, 0);
    }
    public static int getFirstNullLocation(String[][] clothes) {
        return getFirstNullLocation(clothes, 1, 0);
    }





    }
