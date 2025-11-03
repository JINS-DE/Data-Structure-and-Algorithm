import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        char[][] map = new char[N][M];
        for (int i = 0; i<N; i++){
            map[i] = sc.next().toCharArray();
        }

        boolean[] visitedRow = new boolean[N];
        boolean[] visitedCol = new boolean[M];
        // 1. 어디 row, col을 채워야하는지 확인
        for (int i=0; i<N;i++){
            for (int j=0; j<M;j++){
                if (map[i][j]=='X'){
                    visitedRow[i] = true;
                    visitedCol[j] = true;
                }
            }
        }

        // 2. 비어있는 row, col 개수 찾기
        int emptyCountRow=N;
        for (int i=0;i<N;i++) if (visitedRow[i]) emptyCountRow--;
        int emptyCountCol=M;
        for (int i=0;i<M;i++) if (visitedCol[i]) emptyCountCol--;

        // 3. max ( 빈 row 개수, 빈 col 개수)
        System.out.println(Math.max(emptyCountRow, emptyCountCol));

    }
}