import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // 1. 완성까지 남은 일수 계산 배열(d_day) 만들기
        int[] d_day = new int[progresses.length];
        for (int i = 0 ; i < progresses.length; i++){
            int day = 100 - progresses[i];
            if (day%speeds[i]==0){
                d_day[i] = day/speeds[i];
            } else{
                d_day[i] = day/speeds[i]+1;
            }
        }
        
        // 2. d_day 순회
        int progressingIndex = 0;
        List<Integer> answer = new ArrayList<>();
        for (int i=1; i<d_day.length; i++){
            if (d_day[i] > d_day[progressingIndex]){
                answer.add(i-progressingIndex);
                progressingIndex = i;
            }
        }
        // 3. 계산 안된 거 확인 
        if (progressingIndex < d_day.length){
            answer.add(d_day.length-progressingIndex);
        }
        // 4. answer -> int[]
        int[] answerArr = new int[answer.size()];
        for (int i=0; i<answerArr.length;i++){
            answerArr[i] = answer.get(i);
        }
        
        return answerArr;
    }
}