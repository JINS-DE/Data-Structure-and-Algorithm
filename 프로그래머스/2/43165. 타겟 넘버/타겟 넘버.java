import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        return count(numbers,target,0,0);
    }
    
    private int count(int[] numbers, int target, int idx, int sum){
        if (idx>=numbers.length){
            return sum==target ? 1 : 0;
        }
        int plus = count(numbers,target,idx+1,sum+numbers[idx] );
        int minus = count(numbers,target,idx+1,sum-numbers[idx]);
        return plus+minus;
    }
}