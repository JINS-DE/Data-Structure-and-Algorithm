import java.util.*;
class Solution {
    public String solution(String number, int k) {
        int len = number.length();
        int targetLen = len - k;
        StringBuilder sb = new StringBuilder();
        for (int i=0; i < len; i++){
            char curr = number.charAt(i);
            while (sb.length()>0 && sb.charAt(sb.length()-1) < curr && k>0){
                k--;
                sb.deleteCharAt(sb.length()-1);
            }
            sb.append(curr);
        }
        
        return sb.substring(0,targetLen);
    }
}
