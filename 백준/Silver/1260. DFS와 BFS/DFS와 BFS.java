
import java.util.*;
import java.io.*;
public class Main{
    static int N,M,V;
    static List<List<Integer>> adj = new ArrayList<>();
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException{
        input();
        dfs(V);
        System.out.println(sb.toString());
        init();
        bfs(V);
        System.out.println(sb.toString());
    }
    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        // 인접리스트 초기화
        for (int i=0;i<=N;i++){
            adj.add(new ArrayList<>());
        }

        // 방문배열 초기화
        visited = new boolean[N+1];

        // 인접리스트 세팅
        for (int i=0; i<M; i++){
            String[] arr = br.readLine().split(" ");
            int a = Integer.parseInt(arr[0]);
            int b = Integer.parseInt(arr[1]);
            adj.get(a).add(b);
            adj.get(b).add(a);
        }

        // 인접리스트 정렬
        for (int i=0; i<=N;i++){
            Collections.sort(adj.get(i));
        }

    }
    static void dfs(int node){
        visited[node] = true;
        sb.append(node).append(" ");
        for (int nextNode : adj.get(node)){
            if (!visited[nextNode]){
                dfs(nextNode);
            }
        }

    }
    static void bfs(int node){
        Queue<Integer> q = new LinkedList<>();
        q.offer(node);
        visited[node] = true;
        while (!q.isEmpty()){
            int currNode = q.poll();
            sb.append(currNode).append(" ");
            for (int nextNode : adj.get(currNode)){
                if (!visited[nextNode]){
                    visited[nextNode] = true;
                    q.offer(nextNode);
                }
            }
        }
    }

    static void init(){
        visited = new boolean[N+1];
        sb = new StringBuilder();
    }
}