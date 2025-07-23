import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> array = new ArrayList<>();
        int tmp = arr[0];
        array.add(tmp);
        for (int i : arr){
            if (i==tmp){
                continue;
            } else{
                tmp = i;
                array.add(tmp);
            } 
        }
        answer = array.stream().mapToInt(i->i).toArray();

        return answer;
    }
}