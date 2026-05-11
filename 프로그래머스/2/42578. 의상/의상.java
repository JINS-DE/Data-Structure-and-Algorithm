import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Map <String,Integer> hash = new HashMap<>();
        for (String[] arr : clothes){
            String kind = arr[1];
            hash.put(kind,hash.getOrDefault(kind,0)+1);
        }
        int answer = 1;
        for (int count : hash.values()){
            answer *= (count+1);
        }
        return answer-1;
    }
}