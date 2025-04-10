def solution(alp, cop, problems):
    INF = int(1e9)
    MAX_ALP, MAX_COP = 0,0
    for problem in problems:
        MAX_ALP = max(problem[0],MAX_ALP)
        MAX_COP = max(problem[1],MAX_COP)
    
    dp = [[INF]*(MAX_COP+1) for _ in range(MAX_ALP+1)]
    alp = min(MAX_ALP,alp)
    cop = min(MAX_COP,cop)
    dp[alp][cop] = 0
    
    for al in range(alp,MAX_ALP+1):
        for co in range(cop,MAX_COP+1):
            if al < MAX_ALP:
                dp[al+1][co] = min(dp[al][co]+1,dp[al+1][co])
            if co < MAX_COP:                
                dp[al][co+1] = min(dp[al][co]+1,dp[al][co+1])
            
            for alp_req,cop_req, alp_rwd, cop_rwd, cost in problems:
                if al>=alp_req and co>=cop_req:
                    new_al = min(al+alp_rwd,MAX_ALP)
                    new_co = min(co+cop_rwd,MAX_COP)
                    dp[new_al][new_co] = min(dp[al][co]+cost, dp[new_al][new_co])
    return dp[MAX_ALP][MAX_COP]
