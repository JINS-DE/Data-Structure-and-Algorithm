/*

- Map<String,Integer> countReported : hashMap으로 각 아이디마다 신고 받은 횟수 관리
- countReported를 순회하면서 k이상 인애들 찾기

*/
import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String,Set<String>> reportList = new HashMap<>();
        for (String id : id_list){
            reportList.put(id,new HashSet<>());
        }
        
        
        Map<String,Integer> countReported = new HashMap<>();
        StringTokenizer st;
        for (String names : report){
            st = new StringTokenizer(names);
            String reporter = st.nextToken();
            String reported = st.nextToken();
            if (!reportList.get(reporter).contains(reported)){
                countReported.put(reported, countReported.getOrDefault(reported,0)+1);
                reportList.get(reporter).add(reported);
            }
        }
        
        List<String> arr = new ArrayList<>();
        
        for (String id: id_list){
            if (countReported.getOrDefault(id,0) >= k){
                arr.add(id);
            }
        }
        
        int[] answer = new int[id_list.length];
        for (int i=0;i<id_list.length;i++) {
            
            for (String reported : arr){
                if (reportList.get(id_list[i]).contains(reported)){
                    answer[i]+=1;
                }
            }
            
        }
        
        
        return answer;
    }
}