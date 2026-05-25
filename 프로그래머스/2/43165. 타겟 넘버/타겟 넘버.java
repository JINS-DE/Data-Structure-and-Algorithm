import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        return count(numbers,target,0,0,0);
    }
    
    private int count(int[] numbers, int target, int idx, int sum, int answer){
        if (idx>=numbers.length){
            if (sum==target) return 1;
            return 0;
        }
        return count(numbers,target,idx+1,sum+numbers[idx], answer) + count(numbers,target,idx+1,sum-numbers[idx], answer);
    }
}