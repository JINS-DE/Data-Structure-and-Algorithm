import java.io.*;
import java.util.*;

public class Main{

    public static void main(String[] args) throws IOException{
        // input
        // int N, long [] cards
        int N;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        long [] cards = new long[N];
        for (int i=0; i<N;i++){
            cards[i] = Long.parseLong(br.readLine());
        }
        // 정렬
        Arrays.sort(cards);

        // 2번째 원소부터 차례대로 보면서, 같은숫자가 이어서 나오고 있는지, 새로운 숫자가 나왔는 지를 판단하여
        // currentCount 갱신, answer 갱신
        // long answer, int maxCount, int currentCount
        long answer=cards[0];
        int maxCount = 1;
        int currentCount = 1;
        for(int i=1; i<N; i++){
            if (cards[i-1]==cards[i]){
                currentCount++;
            } else{
                currentCount = 1;
            }
            if (maxCount < currentCount){
                answer = cards[i];
                maxCount = currentCount;
            }
        }
        System.out.println(answer);
    }
}