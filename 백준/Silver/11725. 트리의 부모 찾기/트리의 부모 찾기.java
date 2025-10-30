import java.util.*;
public class Main {
    static int N;
    static List<Integer>[] tree;
    static int[] parents;
    static boolean[] check;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        tree = new ArrayList[N+1];
        parents = new int[N+1];
        check = new boolean[N+1];

        for (int i = 0; i <= N; i++) {
            tree[i] = new ArrayList<>();
        }

        for (int i = 0; i < N-1; i++) {
            int node1 = sc.nextInt();
            int node2 = sc.nextInt();
            tree[node1].add(node2);
            tree[node2].add(node1);
        }
        dfs(1);
        for (int i=2;i<=N;i++){
            System.out.println(parents[i]);
        }
    }

    public static void dfs(int node){
        check[node] = true;
        for (int i = 0 ; i < tree[node].size(); i++){
            int child = tree[node].get(i);
            if (!check[child]){
                parents[child] = node;
                dfs(child);
            }
        }
    }
}