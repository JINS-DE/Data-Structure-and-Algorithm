import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(stk.nextToken());
        int Q = Integer.parseInt(stk.nextToken());
        int[] arr = new int[N+1];
        stk = new StringTokenizer(br.readLine());
        for (int i=1;i<=N;i++){
            arr[i] = Integer.parseInt(stk.nextToken());
        }
        int[] prefix = new int[N+1];
        for (int i=1;i<=N;i++){
            prefix[i] = arr[i] ^ prefix[i-1];
        }
        int ans = 0;
        for (int q=0;q<Q;q++){
            stk = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(stk.nextToken());
            int end = Integer.parseInt(stk.nextToken());
            ans ^= prefix[end] ^ prefix[start-1];
        }
        bw.write(ans + "\n");
        bw.flush();
    }
}