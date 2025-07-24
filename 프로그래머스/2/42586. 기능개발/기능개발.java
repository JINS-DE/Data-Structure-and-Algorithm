/*
풀이
1. 각 남은 일 수를 각 배포 우선순위 대로 맞게 remindDayList 데이터 넣어줌.
- 나머지가 있으면 -> 몫+1 없으면 몫

2. beforeRemindDay=remindDayList[0], count=1 초기화
3. remindDayList 순차적으로 for 문을 돌면서 beforeRemindDay보다 크면 큰 숫자로 초기화 시켜주고 count answer에 추가, 더 큰 숫자 나올때 까지 count에 세어준다. 
*/
import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int deploySize = progresses.length;
        int[] remindDayList = new int[deploySize];
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i=0; i < deploySize; i++){
            remindDayList[i] = ((100-progresses[i]) % speeds[i])>0 ? ((100-progresses[i]) / speeds[i])+1 : (100-progresses[i]) / speeds[i];
        }
        
        int beforeRemindDay = remindDayList[0];
        int count = 1;
        int lastIndex = 0;
        for (int i=1;i<deploySize;i++){
            if (remindDayList[i]>beforeRemindDay){
                beforeRemindDay=remindDayList[i];
                answer.add(count);
                count=1;
                lastIndex=i;
            } else {
                count+=1;
            }
        }
        answer.add(deploySize-lastIndex);
        return answer.stream().mapToInt(i->i).toArray();
    }
}