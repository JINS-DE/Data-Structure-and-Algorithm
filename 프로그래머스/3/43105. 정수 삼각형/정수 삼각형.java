import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        for (int i=1; i<triangle.length; i++){
            triangle[i][0]+=triangle[i-1][0];
            triangle[i][i]+=triangle[i-1][i-1];
            for (int j=1; j<triangle[i].length-1; j++){
                triangle[i][j]+=Math.max(triangle[i-1][j-1],triangle[i-1][j]);
            }
        }
        
        int answer = 0;
        int n = triangle.length;
        for (int i=0; i<triangle[n-1].length;i++){
            answer = Math.max(triangle[n-1][i],answer);
        }
        return answer;
    }
}
