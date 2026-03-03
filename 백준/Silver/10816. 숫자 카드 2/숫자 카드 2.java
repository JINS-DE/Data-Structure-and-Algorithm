
import java.io.*;
import java.util.*;
public class Main {
    static int N,M;
    static int[] cards;
    static int[] quests;
    public static void main(String[] args) throws IOException {
        input();
        Arrays.sort(cards);
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<M; i++){
            int num = quests[i];
            sb.append(count(num)).append(" ");
        }
        System.out.println(sb.toString());

    }
    static int count(int num){
        int lower = lowerbound(num);
        int upper = upperbound(num);
        return upper-lower;
    }
    static int lowerbound(int target){
        int left=0, right = N;
        while (left<right){
            int mid = left + (right-left)/2;
            if (cards[mid] < target){
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
    static int upperbound(int target){
        int left=0, right = N;
        while (left<right){
            int mid = left + (right-left)/2;
            if (cards[mid] <= target){
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        cards = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N;i++){
            cards[i] = Integer.parseInt(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());
        quests = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<M;i++){
            quests[i] = Integer.parseInt(st.nextToken());
        }
    }
}
