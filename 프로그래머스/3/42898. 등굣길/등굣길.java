import java.util.*;
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int mod = 1000000007;
        
        // 맵 초기화
        int[][] dp = new int[n+1][m+1];
        
        // 장애물 map 추가
        for (int[] puddle:puddles){
            dp[puddle[1]][puddle[0]] = -1;
        }
        
        dp[1][1] = 1;
        
        // dp[r][c] = dp[r-1][c] + dp[r][c-1]
        for (int r=1;r<=n;r++){
            for (int c=1;c<=m;c++){
                if (dp[r][c]==-1){
                    continue;
                }
                if (r-1>0 && dp[r-1][c]!=-1){
                    dp[r][c]+=dp[r-1][c];
                }
                if (c-1>0 && dp[r][c-1]!=-1){
                    dp[r][c]+=dp[r][c-1];
                }
                dp[r][c] %= mod;
            }
        }
        
        return dp[n][m]%mod;
    }
}