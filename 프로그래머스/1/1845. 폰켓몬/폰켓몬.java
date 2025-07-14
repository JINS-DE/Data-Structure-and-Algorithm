import java.util.*;
class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int n : nums){
            set.add(n);
        }
        return ((nums.length/2)<set.size())?nums.length/2:set.size();
    }
}