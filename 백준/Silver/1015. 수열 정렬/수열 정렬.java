
import java.util.*;
import java.io.*;



public class Main{

    static class Elem implements Comparable<Elem>{
        public int val,idx;
        public Elem(int val, int idx){
            this.val = val;
            this.idx = idx;
        }
        @Override
        public int compareTo(Elem other){
            if (val != other.val) return val-other.val;
            return idx-other.idx;
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer stk = new StringTokenizer(br.readLine());

        Elem[] arr = new Elem[N];
        for (int i = 0; i < N; i++){
            arr[i] = new Elem(Integer.parseInt(stk.nextToken()), i);
        }
        Arrays.sort(arr);
        int[] p = new int[N];
        for (int i=0; i<N;i++){
            p[arr[i].idx] = i;
        }

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<N;i++){
            sb.append(p[i]).append(" ");
        }
        System.out.println(sb);

    }
}