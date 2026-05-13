import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] p1 = {1, 2, 3, 4, 5};
        int[] p2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int s1 = 0; 
        int s2 = 0;
        int s3 = 0;
        for (int i=0; i<answers.length; i++){
            int answer = answers[i];
            if (p1[i%5] == answer) s1++;
            if (p2[i%8] == answer) s2++;
            if (p3[i%10] == answer) s3++;
        }
        
        int max = Math.max(s1,Math.max(s2,s3));
        int cnt = 0;
        if (s1==max) cnt++;
        if (s2==max) cnt++;
        if (s3==max) cnt++;
        int[] answer = new int[cnt];
        
        int i = 0;
        if (s1==max) answer[i++] = 1;
        if (s2==max) answer[i++] = 2;
        if (s3==max) answer[i] = 3;
        
        return answer;
    }
}