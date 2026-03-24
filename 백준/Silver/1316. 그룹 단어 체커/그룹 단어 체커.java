
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
        int len = word.length();
        for (int i=0; i<len; i++){
            char c = word.charAt(i);
            if (set.contains(c)){
                return false;
            }
            set.add(c);
            while (i<len-1){
                char nextChar = word.charAt(i+1);
                if (c==nextChar){
                    i++;
                } else{
                    break;
                }
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
