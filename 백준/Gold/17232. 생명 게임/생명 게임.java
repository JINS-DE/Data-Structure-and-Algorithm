import java.util.*;
import java.io.*;

public class Main{
    static int N,M,T,K,a,b;
    static char[][] map;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        // map 채우기
        map = new char[N+1][M+1];
        for (int i=1;i<=N;i++){
            String line = br.readLine();
            for (int j=1;j<=M;j++){
                map[i][j] = line.charAt(j-1);
            }
        }

        // T 시간 동안 각 칸은 시간마다 아래 상황을 반복
        // 1. 생존 : 현재 칸에 생명 O, a<= 주위생명 <=b 이라면 해당 칸의 생명은 생존
        // 2. 고독 : 현재 칸에 생명 O, 주위생명 < a 해당 칸의 생명은 외로워서 죽음
        // 3. 과밀 : 현재 칸에 생명이 O, b < 주위생명 해당 칸의 생명은 과밀로 죽음
        // 4. 탄생 : 현재 칸에 생명이 X, a < 주위생명 <= b 라면 해당 칸에 생명이 생긴다.
        while (T-- > 0){
            // 2차원 누적합 배열
            int[][] prefixArr = getPrefixArr();
            for (int i=1;i<=N;i++){
                for(int j=1;j<=M;j++){
                    // 주위 생명 개수 카운트 
                    int nearAlive = getCountAlive(prefixArr,i,j);
                    if (map[i][j]=='*'){
                        nearAlive--;
                        if (nearAlive < a || nearAlive > b) map[i][j]='.';
                    } else{
                        if (a<nearAlive && nearAlive<=b){
                            map[i][j] = '*';
                        }
                    }
                }
            }
        }
        // 출력
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                bw.write(map[i][j]);
            }
            bw.newLine();
        }
        bw.flush();
    }

    public static int getCountAlive(int[][] prefix, int r, int c){
        int x1 = Math.max(1,r-K);
        int y1 = Math.max(1,c-K);
        int x2 = Math.min(N,r+K);
        int y2 = Math.min(M,c+K);
        return prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1];
    }

    public static int[][] getPrefixArr(){
        int[][] prefixArr = new int[N+1][M+1];
        for (int i=1;i<=N;i++){
            for (int j=1;j<=M;j++){
                int val = map[i][j]=='*' ? 1 : 0;
                prefixArr[i][j] = val + prefixArr[i][j-1]+ prefixArr[i-1][j] -prefixArr[i-1][j-1];
            }
        }
        return prefixArr;
    }
}