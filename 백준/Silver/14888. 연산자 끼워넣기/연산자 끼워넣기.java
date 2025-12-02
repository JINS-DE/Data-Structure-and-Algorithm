import java.util.*;
import java.io.*;
public class Main{
    static StringBuilder sb = new StringBuilder();
    static int max = -1000000000;
    static int min = 1000000000;
    static int N;
    static int[] arr;
    static int[] calc = new int[4];
    public static void main(String[] args) throws Exception{
        input();
        backtracking(1,arr[0]);
        System.out.println(max);
        System.out.println(min);
    }

    // 입력 받기
    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N= Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0;i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i=0;i<4;i++){
            calc[i] = Integer.parseInt(st.nextToken());
        }
    }

    static void backtracking(int k, int result){
        
        if (k==N){
            max = Math.max(max,result);
            min = Math.min(min,result);
        }


        // +, -, *, /
        for (int j=0;j<4;j++){
            if (calc[j]==0) continue;
            calc[j]--;
            if (j==0){
                backtracking(k+1,result+arr[k]);
            } else if(j==1){
                backtracking(k+1,result-arr[k]);
            } else if(j==2){
                backtracking(k+1,result*arr[k]);
            } else{
                backtracking(k+1,result/arr[k]);
            }
            calc[j]++;
        }


    }
}