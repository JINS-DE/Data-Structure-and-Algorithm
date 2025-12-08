import org.w3c.dom.ls.LSOutput;

import java.util.*;
import java.io.*;

public class Main{
    static int N,S;
    static int ans;
    static int[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stk.nextToken());
        S = Integer.parseInt(stk.nextToken());
        stk = new StringTokenizer(br.readLine());

        arr = new int[N];
        for (int i=0;i<N;i++){
            arr[i] =Integer.parseInt(stk.nextToken());
        }
        recur(0,0);
        if (S==0) ans--;
        System.out.println(ans);
        
    }


    static void recur(int depth,int sum){
        if (depth==N){

            if (sum==S){
                ans++;
            }
            return;
        }
        recur(depth+1,sum);
        recur(depth+1,sum+arr[depth]);
    }
}