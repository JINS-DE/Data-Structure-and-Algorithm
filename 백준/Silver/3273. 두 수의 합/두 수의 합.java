import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Set<Integer> hash = new HashSet<>();

        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int x = Integer.parseInt(br.readLine());

        int ans = 0;
        for (int num:arr){
            if (hash.contains(x-num)) ans++;
            hash.add(num);
        }
        bw.write(String.valueOf(ans));
        bw.flush();

    }
}