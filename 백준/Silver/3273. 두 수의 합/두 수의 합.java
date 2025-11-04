import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Set<Integer> hash = new HashSet<>();
        int n = Integer.parseInt(br.readLine());
        String[] st = br.readLine().split(" ");
        int x = Integer.parseInt(br.readLine());
        
        int ans = 0;
        for (String s : st) {
            int elem = Integer.parseInt(s);
            if (hash.contains(elem)) {
                hash.add(x - elem);
                ans++;
            } else {
                hash.add(x - elem);
            }
        }
        System.out.println(ans);

    }
}