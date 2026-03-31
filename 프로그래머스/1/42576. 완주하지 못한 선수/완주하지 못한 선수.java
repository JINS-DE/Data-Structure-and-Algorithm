import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> hm = new HashMap<>();

        // 1. 모든 참가자 카운팅 (+)
        for (String p : participant) hm.put(p, hm.getOrDefault(p, 0) + 1);
        
        // 2. 완주자 카운팅 (-)
        for (String c : completion) hm.put(c, hm.get(c) - 1);

        // 3. 0이 아닌 (남은 1명) 사람 찾기
        for (String key : hm.keySet()) {
            if (hm.get(key) != 0) return key;
        }

        return "";
    }
}