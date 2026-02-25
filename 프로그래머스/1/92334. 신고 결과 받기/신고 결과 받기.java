/*
신고 당한 횟수 관리
HashMap<String,Integer> reportedCount = new HashMap<>();

내가 신고한 사람들 목록 관리
HashMap<String,Set<String>> reportList = new HashMap<>();
*/

import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        // 0. 초기화 
        int n = id_list.length;
        int[] answer = new int[n];
        Map<String,Set<String>> reportList = new HashMap<>();
        Map<String,Integer> reportedCount = new HashMap<>();
        
        // 1. reportList, reportedCount 데이터 주입
        for (String reportInfo : report){
            String[] tmp = reportInfo.split(" ");
            String reporter = tmp[0];
            String reported = tmp[1];
            
            // 코드 개선할 곳
            Set<String> reportedUserList = reportList.get(reporter);
            if ( reportedUserList == null){
                reportedUserList = new HashSet<>();
                reportList.put(reporter, reportedUserList);
            }
            // 중복 신고 시 reportedCount의 count는 1회 처리 
            if ( !reportedUserList.contains(reported) ){
                reportedUserList.add(reported);
                reportedCount.put(reported,reportedCount.getOrDefault(reported,0)+1);
            }
        }
        
        // 2. reportList 순회하면서 k 값이 넘는 사람이 있으면 answer 추가
        for (int i=0; i<n;i++){
            String user = id_list[i];
            int mailSendCount=0;
            var sets = reportList.get(user);
            if (sets == null) continue;
            for (String reportedUser : sets){
                Integer count = reportedCount.get(reportedUser);
                if (count!=null && count>=k){
                    mailSendCount++;
                }
                
            }
            answer[i] = mailSendCount;
        }
        
        return answer;
    }
}