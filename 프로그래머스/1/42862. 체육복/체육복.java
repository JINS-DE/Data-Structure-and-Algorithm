import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        boolean[] isHaveCloth = new boolean[n];
        boolean[] isRemain = new boolean[n];
        Arrays.fill(isHaveCloth, true);
        Arrays.sort(lost);
        Arrays.sort(reserve);
        for (int r : reserve){
            isRemain[r-1] = true;
        }
        
        for (int l : lost){
            isHaveCloth[l-1] = false;
        }
        
        for (int l : lost){
            if (isRemain[l - 1]) {
                isHaveCloth[l - 1] = true; 
                isRemain[l - 1] = false;  
            }
        }
        
        for (int l : lost){
            if (isHaveCloth[l-1]){
                continue;
            }
            
            // 앞번호
            if (l-2>=0 && isRemain[l-2]){
                isRemain[l-2] = false;
                isHaveCloth[l-1] = true;
            } 
            // 뒷번호
            else if (l < n && isRemain[l]){
                isRemain[l] = false;      
                isHaveCloth[l-1] = true;
            }
        }
        
        int answer = 0;
        for (boolean bool : isHaveCloth) {
            if (bool) answer++;
        }
        
        return answer;
    }
}