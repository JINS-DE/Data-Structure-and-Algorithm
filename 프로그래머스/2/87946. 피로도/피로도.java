import java.util.*;
class Solution {
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        
        return dfs(k,visited,dungeons);
    }
    
    private int dfs(int tired, boolean[] visited, int[][]dungeons){
        int maxCount = 0;
        
        for (int i=0; i<dungeons.length; i++){
            if (!visited[i] && tired >= dungeons[i][0]){
                visited[i] = true;
                
                int count = 1 + dfs(tired - dungeons[i][1], visited, dungeons);
                maxCount = Math.max(maxCount,count);
                
                visited[i] = false;
            }
        }
        return maxCount;
        
    }
}