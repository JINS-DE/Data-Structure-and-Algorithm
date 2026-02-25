/*
신고 당한 횟수 관리
HashMap<String,Integer> reportedCount = new HashMap<>();

내가 신고한 사람들 목록 관리
HashMap<String,Set<String>> reportList = new HashMap<>();

정지당한유저 목록
List<String> stopUserList = new ArrayList<>();
*/

import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        // 0. 초기화 
        int n = id_list.length;
        int[] answer = new int[n];
        HashMap<String,Integer> reportedCount = new HashMap<>();
        HashMap<String,Set<String>> reportList = new HashMap<>();
        List<String> stopUserList = new ArrayList<>();
        // 1. report 순회, reportedCount, reportList 주입
        for (String reportUser : report){
            String[] user = reportUser.split(" ");
            String reporter = user[0];
            String reported = user[1];
            
            // 내가 신고한 목록 reportList
            var set = reportList.get(reporter);
            if (set==null) {
                set = new HashSet<>();
                reportList.put(reporter,set);
                };
            
            if (!reportList.get(reporter).contains(reported)){
                reportedCount.put(reported,reportedCount.getOrDefault(reported,0)+1);    
            }
                    
            set.add(reported);
            // reportList.computeIfAbsent(reporter, k -> new HashSet<>()).add(reported);
        }
        // 2. id_list 순회, reportedCount 체크, 신고 당한 횟수 k 이상인 stopUserList 추가 
        for (int i=0; i<n; i++) {
            String user = id_list[i];
            if (reportedCount.getOrDefault(user,0) >= k){
                stopUserList.add(user);
            }
        }
        
        // 3. id_list 순회 stopUserList count 세주고 answer에 count 추가
        for (int i=0; i<n; i++){
            String user = id_list[i];
            Set<String> set = reportList.get(user);
            if (set==null) continue;
            int count = 0;
            for (String stopUser:stopUserList){
                if (set.contains(stopUser)) count++;
            }
            answer[i] = count;
        }
        
        return answer;
    }
}