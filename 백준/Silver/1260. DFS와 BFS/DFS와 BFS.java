
import java.util.*;

public class Main {

    static int N,M,V;
    static List<List<Integer>> graph;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        V = sc.nextInt();
        graph = new ArrayList<>();
        for (int i=0;i<=N;i++){
            graph.add(new ArrayList<>());
        }

        for (int i=0;i<M;i++){
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        for (int i=1;i<=N;i++){
            Collections.sort(graph.get(i));
        }
        visited = new boolean[N+1];
        dfs(V);
        System.out.println();
        visited = new boolean[N+1];
        bfs(V);
    }
    static void dfs(int node) {
        System.out.print(node + " ");
        visited[node] = true;
        for (int nextNode : graph.get(node)) {
            if (!visited[nextNode]) {
                dfs(nextNode);
            }
        }
    }
    static Queue<Integer> q;
    static void bfs(int node){
        q = new LinkedList<>();
        q.offer(node);
        visited[node] = true;

        while (!q.isEmpty()){
            int now = q.poll();
            System.out.print(now+" ");
            for (int nextNode:graph.get(now)){
                if (!visited[nextNode]){
                    q.offer(nextNode);
                    visited[nextNode]=true;
                }
            }
        }
    }
}
