import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int N = arr[0];
        int B = arr[1];
        StringBuilder sb = new StringBuilder(100);
        while (N>0){
            int mod = N%B;
            if (mod<10){
                sb.append(mod);
            } else {
                sb.append((char)('A'+(mod-10)));
            }
            N/=B;
        }
        System.out.println(sb.reverse());
    }
}