
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        Set<Integer> set = new TreeSet<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i=0; i<N; i++){
            int num = Integer.parseInt(st.nextToken());
            set.add(num);
            arr[i] = num;
        }
        Map<Integer,Integer> map = new HashMap<>();
        int idx=0;
        for (int num : set){
            map.put(num,idx++);
        }


        for (int i=0;i<N;i++){
            bw.write(map.get(arr[i]) + " ");
        }
        bw.flush();

    }
}
