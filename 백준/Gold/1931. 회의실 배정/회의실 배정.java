import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] meetings = new int[N][2];
        for (int i=0; i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            meetings[i][0] = Integer.parseInt(st.nextToken());  // 시작
            meetings[i][1] = Integer.parseInt(st.nextToken());  // 종료
        }

        Arrays.sort(meetings, (o1,o2)->{
            if (o1[1] != o2[1]){
                return o1[1]-o2[1];
            }
            return o1[0]-o2[0];
        });

        int count=0;
        int endTime=0;

        for(int i=0;i<N;i++){
            if(meetings[i][0] >= endTime){
                count++;
                endTime = meetings[i][1];
            }
        }

        System.out.println(count);
    }
}
