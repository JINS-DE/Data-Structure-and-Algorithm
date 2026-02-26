/*
- A가 B에게, B가 A에게 선물 몇번 줬는지 저장소 (내가 선물 준 사람의 리스트)
Map<String,Map<String,Integer>> presentList
(ex) { A:{B:3, C:4}, B:{A:4, C:3} }
- 선물지수 기록 (이번달 준 선물의 수 - 받은 선물의 수)
int[] presentDegree;
*/
import java.util.*;
class Solution {
    public int solution(String[] friends, String[] gifts) {
        // 0. 초기화
        int[] answer = new int[friends.length];
        int[] presentDegree = new int[friends.length];
        Map<String,Map<String,Integer>> presentList = new HashMap<>();
        Map<String,Integer> friendIdx = new HashMap<>();
        for (int i=0; i< friends.length; i++){
            friendIdx.put(friends[i], i);
        }
        
        // 1. 데이터 입력
        for (String gift:gifts){
            String[] users = gift.split(" ");
            String giver = users[0];
            String receiver = users[1];
            
            // 1-1. presentList 추가
            // Map<String,Map<String,Integer>> presentList
            if (!presentList.containsKey(giver)){
                presentList.put(giver,new HashMap<>());
            }
            var receiverList = presentList.get(giver);
            receiverList.put(receiver,receiverList.getOrDefault(receiver, 0)+1);
            
            // 1-2. presentDegree 업데이트
            presentDegree[friendIdx.get(giver)]++;
            presentDegree[friendIdx.get(receiver)]--;
        }
        
        
        // 2. friends 순회, 받을 선물의 수 갱신(max(answer,cnt))
        
        // { A:{B:3, C:4}, B:{A:4, C:3} }
        for (int i=0; i<friends.length-1;i++){
            String a = friends[i];
            for (int j=i+1; j<friends.length;j++){
                String b = friends[j];
                int aScore = presentList.getOrDefault(a,new HashMap<>()).getOrDefault(b,0);
                int bScore = presentList.getOrDefault(b,new HashMap<>()).getOrDefault(a,0);
                int aIdx = friendIdx.get(a);
                int bIdx = friendIdx.get(b);
                if (aScore > bScore){
                    answer[aIdx] ++;
                } else if (bScore> aScore){
                    answer[bIdx] ++;
                } else{
                    if (presentDegree[aIdx] > presentDegree[bIdx]){
                        answer[aIdx] ++;
                    } else if (presentDegree[aIdx] < presentDegree[bIdx]){
                        answer[bIdx] ++;
                    } 
                }
            }
            
        }
        return Arrays.stream(answer).max().orElse(0);
    }
}