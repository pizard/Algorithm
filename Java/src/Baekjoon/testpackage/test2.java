package Baekjoon.testpackage;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class test2 {

	static int length ;

    public static void main(String[] args) throws IOException {

        s.init(System.in);

        int testCase = s.nextInt();


        for(int t = 0; t< testCase; t++) {
            int sx = s.nextInt();
            int sy = s.nextInt();
            int ex = s.nextInt();
            int ey = s.nextInt();

            int circle = s.nextInt();
            int cnt = 0;
            for(int i=0; i< circle; i++) {

                int cx = s.nextInt();
                int cy = s.nextInt();
                int r = s.nextInt();

                int r2 = r*r;
                boolean isIncludeS = Math.pow(sx-cx, 2) + Math.pow(sy - cy, 2) < r2;
                boolean isIncludeE = Math.pow(ex-cx, 2) + Math.pow(ey - cy, 2) < r2;

                if(isIncludeS && isIncludeE) {

                }else if(isIncludeS){
                    cnt++;
                }else if(isIncludeE) {
                    cnt++;
                }
            }

            System.out.println(cnt);
        }
    }

    static class s {
        static BufferedReader reader;
        static StringTokenizer tokenizer;

        static void init(InputStream input) {
            reader = new BufferedReader(
                    new InputStreamReader(input) );
            tokenizer = new StringTokenizer("");
        }

        static String next() throws IOException {
            while ( ! tokenizer.hasMoreTokens() ) {
                tokenizer = new StringTokenizer(
                        reader.readLine() );
            }
            return tokenizer.nextToken();
        }

        static int nextInt() throws IOException {
            return Integer.parseInt( next() );
        }
    }
}
