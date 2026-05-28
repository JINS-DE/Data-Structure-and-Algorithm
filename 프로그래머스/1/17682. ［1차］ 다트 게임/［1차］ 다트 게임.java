import java.util.*;
class Solution {
    public int solution(String dartResult) {
        int before = 0;
        int answer = 0;
        for (int i=1; i<dartResult.length();i++){
            char c = dartResult.charAt(i);
            if (c=='S'||c=='D'||c=='T') {
                int num = (dartResult.charAt(i-1) == '0' && i-2 >= 0 && dartResult.charAt(i-2) == '1') 
                            ? 10 : dartResult.charAt(i-1) - '0';
                if (c=='D') num = num*num;
                if (c=='T') num = num*num*num;
                
                if (i+1<dartResult.length()){
                    if (dartResult.charAt(i+1)=='*'){
                        answer -= before;
                        answer += before*2 + num*2;
                        num*=2;
                    } else if (dartResult.charAt(i+1)=='#'){
                        answer += -num;
                        num = -num;
                    } else{
                        answer += num;
                    }
                } else {
                    answer += num;
                }
                before = num;
            }

        }
        return answer;
    }
}