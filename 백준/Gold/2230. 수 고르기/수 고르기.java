import java.util.*;
import java.io.*;
public class Main{
    static int N,M;
    static Integer[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new Integer[N];
        for (int i=0; i<N; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        int pairIndex = 0;
        int ans = Integer.MAX_VALUE;
        Arrays.sort(arr);
        for (int i=0; i<N-1; i++){
            while (arr[pairIndex]-arr[i] < M && pairIndex < N-1){
                pairIndex++;
            }
            int diff = arr[pairIndex]-arr[i];
            if (diff>=M) ans = Math.min(ans, arr[pairIndex]-arr[i]);
        }
        System.out.println(ans);
    }
}