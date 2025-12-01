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
        int ans = Integer.MAX_VALUE;
        Arrays.sort(arr);
        for (int i=0; i<N-1; i++){
            ans = Math.min(ans, binarySearch(i));
        }
        System.out.println(ans);
    }

    static int binarySearch(int standard){
        int left = standard+1;
        int right = N-1;
        int mid, target;
        int diff = Integer.MAX_VALUE;
        while (left<=right){
            mid = left + (right-left)/2;
            target = arr[mid] - arr[standard];
            if (target < M){
                left = mid+1;
            } else {
                right = mid-1;
                diff = target;
            }

        }
        return diff;
    }
}