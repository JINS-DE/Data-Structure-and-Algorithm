import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        int N = Integer.parseInt(arr[0]);
        int M = Integer.parseInt(arr[1]);

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] heightArr = new int[N+1];
        for (int i=1;i<=N;i++){
            heightArr[i] = Integer.parseInt(st.nextToken());
        }
        int[] prefixArr = new int[N+2];
        for (int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int height = Integer.parseInt(st.nextToken());
            prefixArr[start] += height;
            prefixArr[end+1] -= height;
        }

        for (int i=1;i<=N;i++){
            prefixArr[i] += prefixArr[i-1];
            heightArr[i] += prefixArr[i];
            String output = Integer.toString(heightArr[i]);
            bw.write(output+" ");
        }
        bw.flush();

    }
}