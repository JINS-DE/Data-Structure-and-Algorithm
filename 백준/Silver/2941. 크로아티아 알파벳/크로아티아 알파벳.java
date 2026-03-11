
import java.io.*;
import java.util.*;
public class Main {
    static String st;
    public static void main(String[] args) throws IOException {
        input();
        int N = st.length();
        int answer = 0;
        for (int i=0; i<N;i++){
            if (i==N-1) {
                answer ++;
                break;
            }
            char ch = st.charAt(i);
            char nextChar = st.charAt(i+1);
            if (ch == 'c'){
                if ( nextChar == '=' || nextChar == '-'){
                    i ++;
                }
            } else if( ch == 'd'){
                if ( nextChar == '-'){
                    i++;
                } else if (i+2<N && nextChar == 'z' && st.charAt(i+2) == '='){
                    i+=2;
                }
            } else if( ch == 'l' && nextChar == 'j'){
                i++;
            } else if( ch == 'n' && nextChar == 'j' ){
                i++;
            } else if( ch == 's' && nextChar =='=') {
                i++;
            } else if( ch == 'z' && nextChar =='=') {
                i++;
            }
            answer ++;
        }
        System.out.println(answer);
    }

    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = br.readLine();
    }
}
