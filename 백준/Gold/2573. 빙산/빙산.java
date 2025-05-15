

import java.util.*;

public class Main {
    static int n, m;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        int year = 0;
        while (true) {
            // 빙산 덩어리 개수 확인
            visited = new boolean[n][m];
            int count = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (graph[i][j] > 0 && !visited[i][j]) {
                        dfs(i, j);
                        count++;
                    }
                }
            }

            if (count >= 2) {
                System.out.println(year);
                return;
            }
            if (count == 0) {
                System.out.println(0);
                return;
            }

            // 빙산 녹이기
            int[][] melt = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (graph[i][j] > 0) {
                        int sea = 0;
                        for (int d = 0; d < 4; d++) {
                            int ni = i + dr[d];
                            int nj = j + dc[d];
                            if (ni >= 0 && ni < n && nj >= 0 && nj < m && graph[ni][nj] == 0) {
                                sea++;
                            }
                        }
                        melt[i][j] = sea;
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    graph[i][j] = Math.max(0, graph[i][j] - melt[i][j]);
                }
            }

            year++;
        }
    }

    static void dfs(int r, int c) {
        visited[r][c] = true;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                if (graph[nr][nc] > 0 && !visited[nr][nc]) {
                    dfs(nr, nc);
                }
            }
        }
    }
}
