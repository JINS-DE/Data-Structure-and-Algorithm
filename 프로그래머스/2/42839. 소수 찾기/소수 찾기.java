import java.util.*;
class Solution {
    public int solution(String numbers) {
        Set<Integer> numberSet = new HashSet<>();
        boolean[] visited = new boolean[numbers.length()];
        // 1. 조합 만들기
        dfs(
            numbers,
            "",
            numberSet,
            visited
        );
        
        // 2. 소수 찾기 
        int answer = 0;
        for (int num : numberSet){
            if(isPrime(num)){
                answer++;
            };
        }
        return answer;
    }
    
    private void dfs(String numbers, String curr, Set<Integer> numberSet, boolean[] visited){
        if (!curr.isEmpty()){
            numberSet.add(Integer.parseInt(curr));
        }
        
        for (int i=0; i<numbers.length();i++){
            if (visited[i]){
                continue;
            }
            
            visited[i] = true;
            
            dfs(
                numbers,
                curr + numbers.charAt(i),
                numberSet,
                visited
            );
            
            visited[i] = false;
        }
        
    }
    
    
    private boolean isPrime(int n){
        if (n<2){
            return false;
        }
        for(int i=2; i<=Math.sqrt(n); i++){
            if (n%i==0){
                return false;
            }
        }
        return true;
    }
}