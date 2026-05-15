import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String[] nums = Arrays.stream(numbers).mapToObj(String::valueOf).toArray(String[]::new);
        Arrays.sort(nums, (o1,o2)->
                    (o2+o1).compareTo(o1+o2));
        
        StringBuilder sb = new StringBuilder();
        for (String num:nums){
            sb.append(num);
        }
        if (nums[0].equals("0")) return "0";
        return sb.toString();
    }
}