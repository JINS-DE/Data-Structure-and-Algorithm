

import java.util.Scanner;

public class Main {
    static int N,M;
    static int[][] graph;
    static boolean[] visited;
    static int answer;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N=sc.nextInt();
        M=sc.nextInt();
        graph = new int[N+1][N+1];
        visited=new boolean[N+1];
        for (int i=0;i<M;i++) {
            int scr = sc.nextInt();
            int dst = sc.nextInt();
            graph[scr][dst] = 1;
            graph[dst][scr] = 1;
        }

        for (int i=1;i<=N;i++){
            if (!visited[i]){
                answer++;
                dfs(i);
            }
        }

        System.out.println(answer);
    }

    static void dfs(int node){
        visited[node]=true;
        for(int i=1;i<=N;i++){
            if(graph[node][i]==1 && !visited[i]){
                dfs(i);
            }
        }

    }
}
