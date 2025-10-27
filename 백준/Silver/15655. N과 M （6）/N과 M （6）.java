import java.util.*;
public class Main{
    static int N,M;
    static int[] numbers;
    static int[] outputs;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        numbers = new int[N];
        outputs = new int[M];

        for (int i=0;i<N;i++){
            numbers[i] = sc.nextInt();
        }

        Arrays.sort(numbers);
        recur(0,0);
    }
    public static void recur(int depth,int start){
        if (M==depth){
            for (int i=0;i<M;i++){
                System.out.print(outputs[i]+" ");
            }
            System.out.println();
            return;
        }

        for (int i=start;i<N;i++){
            outputs[depth] = numbers[i];
            recur(depth+1,i+1);
        }
    }

}