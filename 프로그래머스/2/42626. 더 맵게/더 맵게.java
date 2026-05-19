import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        // 1. min heap 만들기 
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int s : scoville){
            minHeap.offer(s);
        }
        
        // 2. min heap 맨 앞이 K보다 크거나 같을 때까지 새로운 음식 만들기(answer 세기)
        while(minHeap.size()>=2 && minHeap.peek() < K){
            int min = minHeap.poll();
            int nextMin = minHeap.poll();
            int combi = min + (nextMin*2);
            minHeap.offer(combi);
            answer++;
        }
        
        // 3. 만들 수 없는 경우
        if (minHeap.peek() < K){
            return -1;
        }
        return answer;
    }
}