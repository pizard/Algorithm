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


    public double[][] makeMatrix2D(String input){
        if("debug".equals(status))
            input = "[[2,1,3],[1,2,4]]"; // 2 by 3 matrix


        String temp = input.replaceAll("\\{", "[");
        temp = temp.replaceAll(" ", "");
        temp = temp.replaceAll("}", "]");

        Stack<Boolean> validation = new Stack<Boolean>();

        double[][] result = new double[2][2];


        String[] temp1= temp.split("]");
        for(int i=0; i<temp1.length;i++){
            String[] temp2 = temp1[i].split("\\[");
            for(int j=0; j<temp2.length; j++){
                validation.push(true);
                if(!"".equals(temp2[j])){
                   String values[] = temp2[j].split(",");
                   for(int v=0; v<values.length;v++){
                       result[i][v] = Double.parseDouble(values[v]);
                   }
                }
            }
            if(validation.empty()){
                return new double[0][0];
            }else{
                validation.pop();
            }

        }
        return  result;
    }





    public double[][] productMatrix2D(double matrix1[][], double matrix2[][]){
        double[][] result = new double[matrix1.length][matrix2[0].length];
        for(int i=0; i<matrix1.length; i++){
            for(int j=0; j<matrix2[0].length; j++){
                for(int x=0; x<matrix1.length; x++) {
                    result[i][j] += matrix1[i][x] * matrix2[x][j];
                }
            }
        }
        return result;
    }




    public double[][][] forRoIAlignXY(double[][][] matrix){
        // (x.location , y.location, value)
        double[][][] result = new double[matrix.length][matrix[0].length][matrix[0][0].length];
        for (int v = 0; v < matrix[0][0].length; v++) { // value
            for(int x=0; x<matrix.length; x++){ // location.x
                for(int y=0; y<matrix[0].length; y++) { // location.y
                    if(v==0){
                        result[x][y][v] = (matrix[0][0][v] + ((y + 0.5) * (matrix[0][matrix.length - 1][v] - matrix[0][0][v])) / matrix[0].length);
                    }else{
                        result[x][y][v] = (matrix[0][0][v] + ((y + 0.5) * (matrix[matrix.length - 1][0][v] - matrix[0][0][v])) / matrix[0].length);
                    }
                }

            }
        }
        return result;
    }


    public void showMatrix3D(double matrix[][][]){
        for(int i=0; i<matrix.length; i++){
            showMatrix2D(matrix[i]);
        }
        System.out.println();
    }

    public void showMatrix2D(double matrix[][]){
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

}
