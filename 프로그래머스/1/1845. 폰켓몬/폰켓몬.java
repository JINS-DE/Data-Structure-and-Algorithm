import java.util.*;
class Solution {
    public int solution(int[] nums) {
        Set<Integer> pocket = new HashSet<>();
        for (int num : nums){
            pocket.add(num);
        }
        
        if (pocket.size() > nums.length / 2){
            return nums.length/2;
        }
        return pocket.size();
    }
}