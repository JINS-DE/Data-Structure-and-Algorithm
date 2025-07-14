import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String,Integer> hash = new HashMap<>();
        for (String c : completion){
            hash.put(c,hash.getOrDefault(c,0)+1);
        }
        for (String p : participant){
            if (hash.get(p)==null || hash.get(p)<=0) return p;
            hash.put(p,hash.get(p)-1);
        }
        return "없음";
        
    }
}