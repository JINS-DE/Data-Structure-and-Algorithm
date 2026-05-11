import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> li = new ArrayList<>();
        int before = -1;
        for (int n : arr){
            if (n==before) continue;
            li.add(n);
            before = n;
        }
        int[] answer = new int[li.size()];
        for (int i=0; i<li.size();i++){
            answer[i] = li.get(i);
        }

        return answer;
    }
}