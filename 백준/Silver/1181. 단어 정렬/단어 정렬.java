import java.util.*;
import java.io.*;

public class Main{

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        String[] words = new String[N];

        for (int i=0; i<N; i++){
            words[i] = br.readLine();
        }

        Arrays.sort(words, new Comparator<String>(){
            @Override
            public int compare(String s1, String s2){
                if (s1.length() == s2.length()) return s1.compareTo(s2);
                return s1.length() - s2.length();
            }
        });

        bw.write(words[0]+"\n");
        for (int i=1;i<N;i++){
            if (!words[i-1].equals(words[i])){
                bw.write(words[i]+"\n");
            }
        }

        bw.flush();
    }
}
