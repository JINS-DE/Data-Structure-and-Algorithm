import java.util.*;

class Solution {
    public int[] solution(String s) {
        // 1. s 파싱 
        String[] split = s.substring(2,s.length()-2).split("\\}\\,\\{");
        int n = split.length;
        
        // 2. 배열 크기별로 정렬
        Arrays.sort(split,(o1,o2)->o1.length()-o2.length());
        
        // 3. a1, a2, a3 순서대로 채우면 됨 - set 자료구조를 사용
        int[] answer = new int[n];
        Set<String> set = new HashSet<>();
        for (int i=0; i<n;i++){
            for (String num : split[i].split(",")){
                if (!set.contains(num)){
                    answer[i] = Integer.parseInt(num);
                    set.add(num);
                    break;
                }
            }
        }
        
        return answer;
    }
}