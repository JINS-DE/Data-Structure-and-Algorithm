
import java.io.*;
import java.util.*;
public class Main {
    static String[] arr;
    public static void main(String[] args) throws IOException{
        input();
        int answer = 0;
        for (String word : arr){
            if(isGroupWord(word)){
                answer++;
            }
        }
        System.out.println(answer);
    }

    static boolean isGroupWord(String word){
        Set<Character> set = new HashSet<>();
        char prev = ' ';
        for (int i=0; i<word.length();i++){
            char now = word.charAt(i);
            if (prev!=now){
                if (set.contains(now)){
                    return false;
                }
                set.add(now);
                prev = now;
            }
        }
        return true;
    }

    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        arr = new String[N];
        for (int i=0; i<N; i++){
            arr[i] = br.readLine();
        }
    }
}
