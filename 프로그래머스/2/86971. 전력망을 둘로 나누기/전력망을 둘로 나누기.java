import java.util.*;
class Solution {
    public int solution(int n, int[][] wires) {
        int answer = 101;
        for (int i=0; i<n-1 ; i++){
            int[] wire = wires[i];
            
            boolean[] visited = new boolean[n-1];
            visited[i] = true;
            int a = dfs(wire[0], wires, visited, 1);
            // System.out.println("a:"+a);
            visited = new boolean[n-1];
            visited[i] = true;
            int b = dfs(wire[1], wires,visited, 1);
            // System.out.println("b:"+b);
            
            answer = Math.min(answer, Math.abs(a - b));
        }
        return answer;
    }
    
    private int dfs(int node, int[][]wires, boolean[] visited, int count){
        // System.out.println("node:"+node);
        for (int i=0; i<wires.length; i++){
            int[] wire = wires[i];
            int n1 = wire[0];
            int n2 = wire[1];
            if (!visited[i] && (node==n1 || node==n2)){
                visited[i] = true;
                count = dfs(node==n1?n2:n1, wires, visited, count+1);
            }
        }
        return count;
    }
}