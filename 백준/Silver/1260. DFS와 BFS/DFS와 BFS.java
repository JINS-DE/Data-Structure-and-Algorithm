import java.util.*;
import java.io.*;

public class Main{
    static int N,M,V;
    static boolean[] visited;
    static List<List<Integer>> adj;
    static BufferedWriter bw;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        V = Integer.parseInt(input[2]);

        adj = new ArrayList<>();
        for (int i=0;i<N+1;i++){
            adj.add(new ArrayList<>());
        }
        StringTokenizer st;
        for (int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adj.get(a).add(b);
            adj.get(b).add(a);
        }

        for (int i=1;i<=N;i++){
            Collections.sort(adj.get(i));
        }

        visited = new boolean[N+1];
        dfs(V);
        bw.newLine();
        visited = new boolean[N+1];
        bfs(V);
        bw.flush();
    }

    static void dfs(int node) throws IOException{
        bw.write(node+" ");
        visited[node] = true;
        for (int nextNode : adj.get(node)){
            if (!visited[nextNode]){
                dfs(nextNode);
            }
        }
    }
    static Queue<Integer> q;
    static void bfs(int node) throws IOException{
        q = new LinkedList<>();
        q.offer(node);
        visited[node]=true;
        while (!q.isEmpty()){
            int now = q.poll();
            bw.write(now+" ");
            for (int nextNode : adj.get(now)){
                if (!visited[nextNode]){
                    visited[nextNode]=true;
                    q.offer(nextNode);
                }
            }
        }
    }
}