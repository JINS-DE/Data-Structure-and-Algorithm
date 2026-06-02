import java.util.*;
class Solution {
    private boolean isFinished = false;
    public String[] solution(String[][] tickets) {
        // tickets 이름순 오름차순 정렬
        Arrays.sort(tickets,(o1,o2)->o1[1].compareTo(o2[1]));
        
        // ICN부터 시작, DFS로 방문
        boolean[] visited = new boolean[tickets.length];
        List<String> path = new ArrayList<>();
        path.add("ICN");
        dfs("ICN",tickets, visited,path);
        
        return path.toArray(new String[0]);
    }
    
    private void dfs(String depart, String[][] tickets, boolean[] visited, List<String> path){
        if (path.size() == tickets.length+1){
            isFinished = true;
            return;
        }
        
        for (int i=0; i<tickets.length; i++){
            String[] arr = tickets[i];
            if (!visited[i] && arr[0].equals(depart)){
                visited[i] = true;
                path.add(arr[1]);
                dfs(arr[1],tickets,visited,path);
                if (isFinished) return;
                path.remove(path.size()-1);
                visited[i] = false;
            }
        }
    }
}