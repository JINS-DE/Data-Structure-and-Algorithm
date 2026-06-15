/*
brown = width*2 + height*2 -4
height = (brown-width*2+4)/2

yellow = (width-2) * (height-2)

*/
import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int width = 0;
        int height = 0;
        for (int wid = 3 ; wid<brown; wid++){
            int hei = (brown-wid*2+4)/2;
            int total = (wid-2) * (hei-2);
            if (total == yellow){
                width = wid;
                height = hei;
                break;
            }
        }
        return new int[]{Math.max(width,height),Math.min(width,height)};
        // return new int[]{1,1};
    }
}