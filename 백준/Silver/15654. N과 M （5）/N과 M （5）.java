import java.util.*;
public class Main{
    static int N,M;
    static int[] numbers;
    static boolean[] visited;
    static int[] output;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        
        numbers = new int[N];
        visited = new boolean[N];
        output = new int[M];
        
        for (int i=0; i<N; i++){
            numbers[i] = sc.nextInt();
        }
        Arrays.sort(numbers);
        recur(0);
    }
    
    public static void recur(int depth){
        // base
        if (M==depth){
        for(int i = 0; i<M; i++){
            System.out.print(output[i] + " ");
        }
        System.out.println();
            return;    
        }
        
        for (int i=0; i<N;i++){
            if(!visited[i]){
                visited[i] = true;
                output[depth] = numbers[i];
                recur(depth+1);
                visited[i] = false;
            }
        }
    }
}