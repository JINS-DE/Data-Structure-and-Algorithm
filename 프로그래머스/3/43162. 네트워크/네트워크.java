class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        for (int i=0; i<n; i++){
            if (!visited[i]){
                answer++;
                dfs(i, n, computers, visited);
            }
            
        }
        return answer;
    }
    
    private void dfs(int curr, int n, int[][] com, boolean[] visited){
        visited[curr] = true;
        for (int next=0; next < n; next++){
            if (com[curr][next]==1 && !visited[next]){
                dfs(next, n, com, visited);
            }
        }
    }
}