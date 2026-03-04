
import java.io.*;
import java.util.*;
public class Main {
    static int N,M;
    static int[] trees;
    public static void main(String[] args) throws IOException {
        input();
        Arrays.sort(trees);
        long left = 0, right = trees[N-1];
        long answer = 0;
        while (left<=right){
            long mid = left + (right-left)/2;
            if (cut(mid) >= M){
                answer=mid;
                left = mid +1;
            } else{
                right = mid - 1;
            }
        }
        System.out.println(answer);
    }
    static long cut(long cutline){
        long total = 0;
        for (int i=0; i<N;i++){
            if (trees[i] > cutline){
                total += trees[i]-cutline;
            }
        }
        return total;
    }
    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split(" ");
        N = Integer.parseInt(arr[0]);
        M = Integer.parseInt(arr[1]);
        trees = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N;i++){
            trees[i] = Integer.parseInt(st.nextToken());
        }
    }
}
