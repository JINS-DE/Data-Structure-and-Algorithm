import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        // 1. 해쉬 "이름" : "나온 횟수"
        Map<String,Integer> hash = new HashMap<>();
        for (String name : participant){
            hash.put(name, hash.getOrDefault(name,0)+1);
        }
        // 2. completion 순회, 해당 해쉬 count -- 
        for (String name : completion){
            hash.put(name,hash.get(name)-1);
        }
        
        // 3. count > 0 return
        for (Map.Entry<String,Integer> entry : hash.entrySet()){
            if (entry.getValue() > 0){
                return entry.getKey();
            }
        }
        return "";
    }
}