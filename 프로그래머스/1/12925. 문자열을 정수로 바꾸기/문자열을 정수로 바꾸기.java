import java.util.*;
class Solution {
    public int solution(String s) {
        
//         System.out.println(s.substring(1));
//         return 1;
        if (s.charAt(0) == '-'){
            return Integer.parseInt(s.substring(1))*-1;
        } 
        return Integer.parseInt(s);
    }
}