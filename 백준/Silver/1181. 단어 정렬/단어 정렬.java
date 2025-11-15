import java.util.*;
import java.io.*;

public class Main{

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        Set<String> set = new HashSet<>();
        for (int i=0;i<N;i++){
            set.add(br.readLine());
        }
        String[] arr = set.toArray(new String[0]);

        Arrays.sort(arr,(o1,o2)-> {
            if (o1.length() == o2.length()) return o1.compareTo(o2);
            return o1.length()-o2.length();
        });

        for (String st : arr){
            bw.write(st+"\n");
        }
        bw.flush();

    }
}
