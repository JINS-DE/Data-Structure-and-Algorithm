import java.util.*;
class Solution {
    int answer = -1;
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        dfs(0,k,visited,dungeons);
        return answer;
    }
    
    private void dfs(int depth, int tired, boolean[] visited, int[][]dungeons){
        answer = Math.max(answer,depth);
        for (int i=0; i<dungeons.length; i++){
            if (!visited[i] && dungeons[i][0] <= tired){
                visited[i] = true;
                dfs(depth+1, tired-dungeons[i][1], visited, dungeons);
                visited[i] = false;
            }
        }
        
    }
}