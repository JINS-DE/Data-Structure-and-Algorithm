import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> q = new LinkedList<>();
        for (int i=0;i<priorities.length;i++){
            q.offer(new int[]{i,priorities[i]}); // [인덱스, 우선순위]
        }
        
        int answer = 0;
        while(!q.isEmpty()){
            // System.out.println("test");
            int[] arr = q.poll();
            boolean isMax = true;
            
            for (int[] tmp : q){
                if (arr[1]<tmp[1]){
                    isMax = false;
                    break;
                }
            }
            if (isMax){
                answer+=1;
                if(arr[0]==location){
                    return answer;
                }
                
            } else{
                q.offer(arr);
            }
        }
        
        return answer;
    }
}