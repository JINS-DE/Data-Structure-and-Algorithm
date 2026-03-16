
import java.io.*;
import java.util.*;
public class Main {
    static int N,K,L;
    static int[][] board;
    static Map<Integer, Character> changeDirect = new HashMap<>();
    static Queue<int[]> path = new LinkedList<>();
    static int directPoint = 0;
    static int[] dr = {0,1,0,-1};
    static int[] dc = {1,0,-1,0};
    static int answer = 0;
    public static void main(String[] args) throws IOException{
        input();
        // board : 뱀이 있는 곳은 1, 사과는 2
        int pr=1, pc = 1;

        while (true){
            int nr = pr + dr[directPoint];
            int nc = pc + dc[directPoint];
            // 1. 머리 이동 가능한지 체크 후 머리 이동
            if (isMoveCheck(nr,nc)){
                // 2. 사과 있는지 체크 후 없으면 꼬리 이동
                if (!isExistApple(nr,nc)){
                    tailMove();
                }
                board[nr][nc] = 1;
                path.offer(new int[]{nr,nc});
                pr = nr;
                pc = nc;
            } else{
                break;
            }
            answer ++;
            // 3. 방향 체크
            if (changeDirect.containsKey(answer)){
                if(changeDirect.get(answer) == 'L'){
                    directPoint = (directPoint+3)%4;
                } else{
                    directPoint = (directPoint+1)%4;
                }
            }
        }
        System.out.println(answer+1);

    }
    static void tailMove(){
        int[] arr = path.poll();
        board[arr[0]][arr[1]] = 0;
    }
    static boolean isExistApple(int r, int c){
        return board[r][c] == 2;
    }
    static boolean isMoveCheck(int r, int c){
        return !(r==0 || c==0 || r==N+1 || c == N+1 || board[r][c] == 1);
    }
    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        // board 초기화
        board = new int[N+1][N+1];
        int[] coordinate = new int[]{1,1};
        path.offer(coordinate);
        board[1][1] = 1;
        // 사과 위치 저장
        K = Integer.parseInt(br.readLine());
        for (int i=0; i<K; i++){
            String[] arr = br.readLine().split(" ");
            int r = Integer.parseInt(arr[0]);
            int c = Integer.parseInt(arr[1]);
            board[r][c] = 2;
        }
        // 뱀의 방향 변환 정보 저장 (배열 저장)
        L = Integer.parseInt(br.readLine());
        for (int i=0; i<L; i++){
            String[] arr = br.readLine().split(" ");
            changeDirect.put(Integer.parseInt(arr[0]), arr[1].charAt(0));
        }

    }
}