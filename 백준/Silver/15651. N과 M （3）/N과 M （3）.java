import java.util.*;
import java.io.*;
public class Main{
    static StringBuilder sb = new StringBuilder();
    static int N,M;
    static int[] selected;
    public static void main(String[] args) throws Exception{
        input();
        backtracking(1);
        System.out.println(sb.toString());
    }

    // 입력 받기
    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        selected = new int[M+1];
    }

    static void backtracking(int k){
        if (k>M){
            for (int i=1;i<=M;i++){
                sb.append(selected[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i=1; i<=N; i++){
            selected[k] = i;
            backtracking(k+1);
        }
    }
}