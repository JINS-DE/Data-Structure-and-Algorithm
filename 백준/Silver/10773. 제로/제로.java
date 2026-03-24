
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        int answer = 0;

        Deque<Integer> stack = new ArrayDeque<>();
        for (int i=0; i<K; i++){
            int num = Integer.parseInt(br.readLine());
            if (num==0){
                stack.pop();
            } else{
                stack.push(num);
            }

        }
        for (int n: stack){
            answer+=n;
        }
        System.out.println(answer);
    }


}
