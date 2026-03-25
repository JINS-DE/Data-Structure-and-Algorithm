

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
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : st.toCharArray()){
            if (c=='('){
                stack.push('(');
            } else{
                if ( !stack.isEmpty() ){
                    char popC = stack.pop();
                    if (popC == ')'){
                        return false;
                    }
                } else{
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
