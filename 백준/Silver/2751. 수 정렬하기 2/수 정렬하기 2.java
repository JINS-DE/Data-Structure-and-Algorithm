import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        // int[] 사용시 시간 초과 
        // int[] arr = new int[N]; 
        Integer[] arr = new Integer[N];
        for(int i=0;i<N;i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr); // Primitive 배열 시 Dual-Pivot Quick Sort 사용 : 최악의 경우 N^2, 시간 초과
        for (int i=0;i<N;i++){
            bw.write(arr[i] + "\n");
        }
        bw.flush();
    }
}