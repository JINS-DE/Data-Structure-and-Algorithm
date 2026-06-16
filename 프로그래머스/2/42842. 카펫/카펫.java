/*

totalCells = brown + yellow
width = totalCells/height

# height의 최대값 
height * width = totalCells
height*height <= height*width = totalCells (가로가 세로보다 무조건 크다는 조건이 있음)
height^2 <= totalCells
height <= 루트 totalCells 성립

yellow = (width-2) * (height-2)

*/
import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int totalCells = brown + yellow;
        
        for (int height = 3; height <= Math.sqrt(totalCells); height++){
            int width = totalCells / height;
            
            if( (width-2)*(height-2) == yellow){
                return new int[]{width,height};
            }
        }
        return new int[0];
    }
}