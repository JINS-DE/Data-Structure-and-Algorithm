import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        boolean[] visited = new boolean[words.length];
        Queue<int[]> q = new LinkedList<>();
        offerQ(q,begin,words,visited,0);
        while (!q.isEmpty()){
            int[] arr = q.poll();
            String word = words[arr[0]];
            int depth = arr[1];
            if (word.equals(target)){
                answer = depth;
                break;
            }
            offerQ(q,word,words,visited,depth);
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
            }
        }
        return cnt == 1 ? true : false;
    }
    
    void offerQ(Queue<int[]> q, String word, String[] words, boolean[] visited, int depth){
        for (int i=0; i<words.length; i++){
            String target = words[i];
            if (!visited[i] && checkWord(word, target)){
                q.offer(new int[]{i,depth+1});
                visited[i] = true;
            };
        }
    }
}
