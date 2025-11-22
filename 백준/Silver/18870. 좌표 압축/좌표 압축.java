
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int [][] arr = new int[N][2];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int i =0;
        while(st.hasMoreTokens()){
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = i;
            i++;
        }
        Arrays.sort(arr,(o1,o2)->o1[0]-o2[0]);
        int[] answer = new int[N];
        answer[arr[0][1]] = 0;
        int pressIdx = 0;
        for (int j=1; j<N;j++){
            if (arr[j-1][0] != arr[j][0]) {
                pressIdx++;
            }
            answer[arr[j][1]] = pressIdx;
        }
        for (int j=0;j<N;j++){
            bw.write(answer[j] +" ");
        }
        bw.flush();
    }
}
