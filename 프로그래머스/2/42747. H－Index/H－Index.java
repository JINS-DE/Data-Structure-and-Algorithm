import java.util.*;
class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int len = citations.length;
        for (int i=0; i<len; i++){
            int h =len-i;
            if (citations[i]>=h){
                return h;
            }
        }
        
        return 0;
    }
}