import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr= new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int left=0;
        int sum = 0;
        int ans = Integer.MAX_VALUE;

        for (int right=0; right<N; right++){
            sum += arr[right];

            while (sum>=M){
                ans = Math.min(ans, right-left+1);
                sum-=arr[left];
                left++;
            }
        }
        System.out.println(ans==Integer.MAX_VALUE?0:ans);
    }
}