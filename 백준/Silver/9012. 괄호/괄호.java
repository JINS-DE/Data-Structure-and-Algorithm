
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i=0; i<T; i++){
            String st = br.readLine();
            System.out.println(check(st) ? "YES" : "NO");
        }
    }

    static boolean check(String st){
        int count = 0;
        for (char c : st.toCharArray()){
            if (c=='('){
                count++;
            } else{
                if (count ==0) return false;
                count--;
            }
        }
        return count==0;
    }
}
