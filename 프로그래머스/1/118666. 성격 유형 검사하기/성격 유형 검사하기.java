/* 문제 분석 
MBTI 같은 성격 유형 검사 
1. 각 지표에서 더 높은 점수가 검사자의 성격 유형 
2. 같으면 사전순으로 빠른순

생각할점
RN, NR 이런식으로 survey가 나오기에 이에 맞춰서 choices 선택을 잘해줘야함
*/

/* 문제 풀이 
질문 점수 고정 배열 선언 : score
각 성격 검사의 점수를 해쉬로 관리
choices에서 4보다 크면 "AN" -> N에 해당 score 부여, 4보다 작으면 "A"에 해당 score 부여 

1. 질문 점수 고정 배열 선언 : standardScore
2. 각 성격 점수의 hash 관리 : 
3. survey를 돌면서 해당 choices에 맞게 해쉬로 관리된 성격 점수에 점수 부여
*/

import java.util.*;
import java.io.*;
class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        int[] standardScore = {0,3,2,1,0,1,2,3};
        String[] standardPersonality = {"RT","CF","JM","AN"};
        HashMap<String,Integer> personality = new HashMap<>();
        
        // 각 성격마다 점수 부여 로직
        for (int i=0; i<survey.length;i++){
            // System.out.println(i);
            int checkedScoreIndex = choices[i];
            String key0 = Character.toString(survey[i].charAt(0));
            String key1 = Character.toString(survey[i].charAt(1));
            if (checkedScoreIndex<4){
                personality.put(key0, personality.getOrDefault(key0, 0) + standardScore[checkedScoreIndex]);
                personality.putIfAbsent(key1, 0);
            } else {
                personality.put(key1,personality.getOrDefault(key1,0)+standardScore[checkedScoreIndex]);
                personality.putIfAbsent(key0, 0);
            }
        }
        
        // 성격마다 점수 비교하기 
        for (String p : standardPersonality){
            String c_0 = p.substring(0,1);
            String c_1 = p.substring(1,2);
            int score_0 = personality.getOrDefault(c_0,0);
            int score_1 = personality.getOrDefault(c_1,0);
            
            if (score_0 >= score_1){
                answer += c_0;
            } else{
                answer += c_1;
            }
        }
        
        return answer;
    }
}