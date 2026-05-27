import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) return 0;
        int answer = 0;
        boolean[] visited = new boolean[words.length];
        Queue<String[]> q = new LinkedList<>();
        q.offer(new String[]{begin,"0"});
        
        while (!q.isEmpty()){
            String[] arr = q.poll();
            String word = arr[0];
            int depth = Integer.parseInt(arr[1]);
            
            if (word.equals(target)) return depth;
            
            for (int i=0; i<words.length; i++){
                if (!visited[i] && checkWord(word,words[i])){
                    visited[i] = true;
                    q.offer(new String[]{words[i], String.valueOf(depth + 1)});
                }
            }
        }
        
        return answer;
    }
    boolean checkWord(String word, String target){
        int cnt=0;
        for (int i=0; i<word.length(); i++){
            char a = word.charAt(i);
            char b = target.charAt(i);
            if (a!=b){
                cnt++;
                if (cnt > 1) return false;
            }
        }
        return cnt == 1;
    }
}
