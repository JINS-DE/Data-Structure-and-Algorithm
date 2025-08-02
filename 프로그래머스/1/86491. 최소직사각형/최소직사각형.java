import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int max_weight=0;
        int max_height=0;
        for (int i=0;i<sizes.length;i++){
            int w = sizes[i][0];
            int h = sizes[i][1];
            
            int width = Math.max(w,h);
            int height = Math.min(w,h);
            
            max_weight = Math.max(max_weight,width);
            max_height = Math.max(max_height,height);
            
            
            
        }
        return max_weight*max_height;
    }
}