import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String,Integer> hash = new HashMap<>();
        for (String p : participant){
            hash.put(p,hash.getOrDefault(p,0) + 1);
        }
        for (String c : completion){
            int cnt = hash.get(c);
            cnt --;
            if (cnt<=0){
                hash.remove(c);
            } else{
                hash.put(c,cnt);
            }
        }
        String answer="";
        for (String s : hash.keySet()){
            answer = s;
        }
        return answer;
    }
}