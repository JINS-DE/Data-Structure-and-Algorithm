import java.util.*;
class Solution {
    public int solution(int N, int number) {
        if (N==number){
            return 1;
        }
        
        Set<Integer>[] dp = new Set[9];
        for (int i=1;i<9;i++){
            dp[i] = new HashSet<>();
        }
        
        for (int i=1;i<9;i++){
            dp[i].add(getSequnceNumber(N,i));
            for (int j=1; j<i; j++){
                Set<Integer> a = dp[j];
                Set<Integer> b = dp[i-j];
                
                for (int num1 : a){
                    for (int num2 : b){
                        dp[i].add(num1+num2);
                        dp[i].add(num1-num2);
                        dp[i].add(num1*num2);
                        if (num2!=0){
                            dp[i].add(num1/num2);
                        }
                    }
                }
            }
            if (dp[i].contains(number)){
                return i;
            }
        }
        
        return -1;
    }
    
    private int getSequnceNumber(int N, int count){
        int result = 0;
        for (int i=0;i<count;i++){
            result = result*10 + N;
        }
        return result;
    }
}