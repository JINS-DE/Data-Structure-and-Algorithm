
import java.io.*;
import java.util.*;
public class Main {
    static int N,M;
    static int r,c,d;
    static int[][] map;
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,1,0,-1};
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        input();
        while (true){
            if (map[r][c] == 0){
                answer ++;
                map[r][c] = 2;
            } else if (map[r][c] == 1){
                break;
            }

            if (isExistCleanRoom()){
                d = (d-1+4)%4;
                if (map[r+dr[d]][c+dc[d]]==0){
                    r = r + dr[d];
                    c = c + dc[d];
                }
            } else{
                int b = (d+2)%4;
                if (map[r+dr[b]][c+dc[b]] != 1 ){
                    r += dr[b];
                    c += dc[b];
                } else{
                    break;
                }
            }
        }
        System.out.println(answer);
    }

    static boolean isExistCleanRoom(){
        for (int i=0;i<4;i++){
            if (map[r+dr[i]][c+dc[i]] == 0){
                return true;
            }
        }
        return false;
    }
    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split(" ");
        N = Integer.parseInt(arr[0]);
        M = Integer.parseInt(arr[1]);

        arr = br.readLine().split(" ");
        r = Integer.parseInt(arr[0]);
        c = Integer.parseInt(arr[1]);
        d = Integer.parseInt(arr[2]);

        map = new int[N][M];
        for (int i=0; i<N; i++){
            arr = br.readLine().split(" ");
            for (int j=0; j<M; j++){
                map[i][j] = Integer.parseInt(arr[j]);
            }
        }
    }
}