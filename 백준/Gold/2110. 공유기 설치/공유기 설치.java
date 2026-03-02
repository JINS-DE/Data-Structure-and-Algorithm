
import java.io.*;
import java.util.*;
public class Main {
    static int N,C;
    static int[] map;
    public static void main(String[] args) throws IOException {
        input();
        Arrays.sort(map);

        int left=0;
        int right = map[N - 1] - map[0] + 1;
        while (left < right){
            int mid = left + (right-left)/2;
            if (can(mid) < C){
                right = mid;
            } else {
                left = mid +1;
            }
        }
        System.out.println(left-1);

    }
    static int can(int dist){
        int cnt = 1;
        int lastLocate = map[0];
        for (int i=1; i<N;i++){
            int currLocate = map[i];

            if (currLocate - lastLocate >= dist){
                cnt ++;
                lastLocate = currLocate;
            }
        }
        return cnt;
    }
    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split(" ");
        N = Integer.parseInt(arr[0]);
        C = Integer.parseInt(arr[1]);
        map = new int[N];
        for (int i=0; i<N; i++){
            map[i] = Integer.parseInt(br.readLine());
        }
    }
}
