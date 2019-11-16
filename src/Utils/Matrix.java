package Utils;

import sun.lwawt.macosx.CPrinterDevice;

import java.util.Stack;

public class Matrix {

//    matrix[x][y] : 3 by 4 matrix
//       y 0  1  2  3
//    x   ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
//    0 ⎪  1  2  3 -1
//    1 ⎪  2  3  1  2
//    2 ⎪  0 -4  0  1
//

    // status : debug/running
    private static String status = "running";


    public float[][] makeMatrix2D(String input_string){
        if("debug".equals(status))
            input_string = "[[2,1,3],[1,2,4]]"; // 2 by 3 matrix


        String temp = input_string.replaceAll("\\{", "[");
        temp = temp.replaceAll("}", "]");

        Stack<Boolean> validation = new Stack<Boolean>();

        float[][] result = new float[2][3];
        String[] temp1= temp.split("]");
        for(int i=0; i<temp1.length;i++){
            String[] temp2 = temp1[i].split("\\[");
            for(int j=0; j<temp2.length; j++){
                validation.push(true);
                if(!"".equals(temp2[j])){
                   String values[] = temp2[j].split(",");
                   for(int v=0; v<values.length;v++){
                       result[i][v] = Float.parseFloat(values[v]);
                   }
                }
            }
            if(validation.empty()){
                return new float[0][0];
            }else{
                validation.pop();
            }

        }
        return  result;
    }

    public void showMatrix2D(float matrix[][]){
        System.out.println("---------------- (x ,y) Matrix ----------------");
        System.out.print("   ");
        for(int k=0; k<matrix[0].length;k++){
            System.out.printf("%7d", k);
        }
        System.out.println();

        for(int i=0; i<matrix.length; i++){
            System.out.print(i + "  ");
            for(int j=0; j<matrix[0].length; j++){
                System.out.printf("  %.3f", matrix[i][j]);
            }
            System.out.println();
        }
        System.out.println("-----------------------------------------------");
    }


    public float[][] productMatrix2D(float matrix1[][], float matrix2[][]){
        float[][] result = new float[matrix1.length][matrix2[0].length];
        for(int i=0; i<matrix1.length; i++){
            for(int j=0; j<matrix2[0].length; j++){
                for(int x=0; x<matrix1.length; x++) {
                    result[i][j] += matrix1[i][x] * matrix2[x][j];
                }
            }
        }
        return result;
    }
}
