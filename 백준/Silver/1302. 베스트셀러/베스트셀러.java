
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        Map<String,Integer> hash = new HashMap<>();
        for (int i=0; i<N;i++){
            String book = br.readLine();
            hash.put(book,hash.getOrDefault(book,0)+1);
        }
        List<Map.Entry<String,Integer>> entries = new ArrayList<>(hash.entrySet());
        Collections.sort(entries, (o1, o2) -> {
            int count1 = o1.getValue();
            int count2 = o2.getValue();
            if(count1!=count2){
                return count2-count1;
            } else{
                return o1.getKey().compareTo(o2.getKey());
            }
        });
        bw.write(entries.get(0).getKey());
        bw.flush();
    }
}
