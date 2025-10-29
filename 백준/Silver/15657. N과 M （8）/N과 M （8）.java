import java.util.*;
class Main{
    static int N,M;
    static int[] arr;
    static int[] output;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        arr = new int[N];
        output = new int[M];
        for (int i=0; i<N;i++){
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        recur(0,0);
        System.out.print(sb);
    }
    static StringBuilder sb = new StringBuilder();
    public static void recur(int depth, int start){
        if (depth == M){
            for (int j=0;j<M;j++){
                sb.append(output[j]+" ");
            }
            sb.append('\n');
            return;
        }

        for (int i=start; i<N; i++){
            output[depth] = arr[i];
            recur(depth+1,i);
        }
    }
}