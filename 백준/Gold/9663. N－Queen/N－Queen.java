/*
백트레킹 구현
- depth는 row를 의미
- 각 row 마다 반복문으로 col을 움직이며 퀸을 놓을 수 있는지 없는지 체크
    - 놓을 수 있다면 다음 row로 재귀함수
- 퀸을 놓을 수 있는지 없는지 체크 (row는 depth로 계속 이동하기에 안겹침)
    1. col 체크
    2. 정방향 대각선 체크
        - row, col 합이 같음
    3. 역방향 대각선 체크
        - row, col 차가 같음

(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
(3,0) (3,1) (3,2) (3,3)
- 필요 변수 : N, answer, row, col, colChecked 배열, rightDiagonal 배열, reverseDiagonal 배열

* */

import java.util.*;
import java.io.*;
public class Main{
    static int N;
    static int answer;
    static boolean[] colChecked, rightDiagonal, reverseDiagonal;
    public static void main(String[] args) throws Exception{
        input();
        colChecked = new boolean[N];
        rightDiagonal = new boolean[2*N-1];
        reverseDiagonal = new boolean[2*N-1];
        backtracking(0);
        System.out.println(answer);
    }

    // 입력 받기
    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N= Integer.parseInt(br.readLine());
    }

    static void backtracking(int row){
        if (row==N){
            answer++;
            return;
        }
        for (int col=0;col<N;col++){
            if (!colChecked[col] && !rightDiagonal[row+col] && !reverseDiagonal[row-col+(N-1)]){
                colChecked[col] = true;
                rightDiagonal[row+col] = true;
                reverseDiagonal[row-col+(N-1)] = true;
                backtracking(row+1);
                colChecked[col] = false;
                rightDiagonal[row+col] = false;
                reverseDiagonal[row-col+(N-1)] = false;
            }
        }
    }
}