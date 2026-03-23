
import java.io.*;
import java.util.*;
public class Main {
    static String alpha;
    public static void main(String[] args) throws IOException{
        input();
        int N = alpha.length();
        int answer = N;
        for (int i=0; i<N-1;i++){
            char c = alpha.charAt(i);
            char next = alpha.charAt(i+1);

            if (c=='s' || c=='z'){
                if ( next == '='){
                    answer --;
                    i++;
                }
            } else if (c=='c'){
                if (next == '=' || next=='-'){
                    answer--;
                    i++;
                }
            } else if (c=='l' || c=='n'){
                if ( next == 'j'){
                    answer --;
                    i++;
                }
            } else if (c=='d') {
                if (next == '-') {
                    answer--;
                    i++;
                } else if (i+2<N && next == 'z' && alpha.charAt(i+2)=='=') {
                    answer -=2;
                    i+=2;
                }

            }
        }
        System.out.println(answer);
    }



    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        alpha = br.readLine();
    }
}
