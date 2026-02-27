import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> results = new ArrayList<>();
        
        // 1. today 정수로 나타내기
        int todayInt = dayToInt(today);
        
        // 2. terms HashMap으로 관리
        Map<String, Integer> hash = new HashMap<>();
        for (String term : terms) {
            String[] arr = term.split(" ");
            // 유효기간(달) * 28일
            hash.put(arr[0], Integer.parseInt(arr[1]) * 28);
        }
        
        // 3. privacies 순회
        for (int i = 0; i < privacies.length; i++) {
            String[] arr = privacies[i].split(" ");
            int startDate = dayToInt(arr[0]);
            int duration = hash.get(arr[1]);
            
            // 3-2. (수집일 + 유효기간)이 오늘보다 작거나 같으면 만료
            if (startDate + duration <= todayInt) {
                results.add(i + 1); 
            }
        }
        
        // List<Integer>를 int[]로 변환
        return results.stream().mapToInt(Integer::intValue).toArray();
    }

    int dayToInt(String day) {
        String[] arr = day.split("\\.");
        int y = Integer.parseInt(arr[0]);
        int m = Integer.parseInt(arr[1]);
        int d = Integer.parseInt(arr[2]);
        return (y * 12 * 28) + (m * 28) + d;
    }
}