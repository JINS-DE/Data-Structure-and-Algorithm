import java.util.*;

public class Main{
    static int N;
    static int M;
    static int[] arr;
    static int[] output;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        arr = new int[N];
        output = new int[M];
        for (int i=0;i<N;i++){
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        recur(0);
        System.out.print(sb);
    }
    static StringBuilder sb = new StringBuilder();
    public static void recur(int depth){
        if (depth==M){
            for (int i=0;i<M;i++){
                sb.append(output[i] + " ");
            }
            sb.append("\n");
            return;
        }

        for (int i=0; i<N;i++){
            output[depth]=arr[i];
            recur(depth+1);
        }
    }
}