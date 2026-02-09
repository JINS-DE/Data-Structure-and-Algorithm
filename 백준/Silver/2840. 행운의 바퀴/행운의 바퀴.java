

import java.io.*;
import java.util.*;

public class Main{
    static int N,K;
    static int index=0;
    static char[] wheel;
    static int[] shift;
    static char[] alpha;
    static boolean flag;
    static boolean[] used = new boolean[26];


    public static void main(String[] args) throws IOException{
        input();
        flag = rotation();
        if (flag){
            printWheel();
        } else{
            System.out.println("!");
        }
    }
    static boolean rotation(){
        for (int i=0; i<K;i++){
            int moveIndex = (index+shift[i])%N;
            if (wheel[moveIndex]=='?'){
                if (used[alpha[i]-'A']) return false;
                wheel[moveIndex] = alpha[i];
                used[alpha[i]-'A'] = true;
            } else if (wheel[moveIndex] != alpha[i]){
                return false;
            }
            index = moveIndex;
        }
        return true;
    }

    static void printWheel(){
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            int pos = (index - i + N) % N;
            sb.append(wheel[pos]);
        }

        System.out.println(sb.toString());
    }

    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        wheel = new char[N];
        for (int i=0;i<N;i++){
            wheel[i]='?';
        }

        shift = new int[K];
        alpha = new char[K];

        for (int i=0;i<K;i++){
            st = new StringTokenizer(br.readLine());
            shift[i] = Integer.parseInt(st.nextToken());
            alpha[i] = st.nextToken().charAt(0);
        }

    }
}