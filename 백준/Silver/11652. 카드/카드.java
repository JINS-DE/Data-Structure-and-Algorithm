import java.io.*;
import java.util.HashMap;

public class Main{

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        HashMap<Long,Long> hash = new HashMap<>();
        for (int i=0; i<N; i++){
            Long key = Long.parseLong(br.readLine());
            hash.put(key, hash.getOrDefault(key,0L) + 1);
        }
        long maxValue = 0;
        long maxCount = 0;
        for (long val : hash.keySet()){
            long cnt = hash.get(val);
            if (maxCount < cnt){
                maxValue = val;
                maxCount = cnt;
            } else if(maxCount == cnt && maxValue > val ){
                maxValue = val;
            }
        }

        System.out.println(maxValue);
    }
}