
import java.io.*;
import java.util.*;
public class Main {
    static int N,M;
    static int[] budgets;
    public static void main(String[] args) throws IOException {
        input();
        int left = 0, right = Arrays.stream(budgets).max().getAsInt()+1;
        while (left<right){
            int limit = left + (right-left)/2;
            long total = 0;
            for (int budget : budgets){
                if (limit > budget){
                    total += budget;
                } else {
                    total += limit;
                }
            }
            if (total <= M){
                left = limit + 1;
            } else {
                right = limit;
            }
        }
        System.out.println(right-1);
    }

    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        budgets = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N;i++){
            budgets[i] = Integer.parseInt(st.nextToken());
        }
        M = Integer.parseInt(br.readLine());

    }
}
