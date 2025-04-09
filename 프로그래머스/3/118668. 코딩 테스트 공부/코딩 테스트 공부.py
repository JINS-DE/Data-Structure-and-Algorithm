def solution(alp, cop, problems):
    max_alp,max_cop=0,0
    for problem in problems:
        max_alp=max(max_alp,problem[0])
        max_cop=max(max_cop,problem[1])
    
    dp = [[10e9]*(max_cop+1) for _ in range(max_alp+1)]
    alp=min(alp,max_alp)
    cop=min(cop,max_cop)
    dp[alp][cop]=0
    
    for algo in range(alp,max_alp+1):
        for code in range(cop,max_cop+1):
            if algo < max_alp:
                dp[algo+1][code]=min(dp[algo+1][code],dp[algo][code]+1)
            if code < max_cop:
                dp[algo][code+1]=min(dp[algo][code+1],dp[algo][code]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if algo>= alp_req and code>=cop_req:
                    next_alp = min(algo+alp_rwd, max_alp)
                    next_cop = min(code+cop_rwd, max_cop)
                    dp[next_alp][next_cop] = min(dp[algo][code]+cost,dp[next_alp][next_cop])
    
    return dp[max_alp][max_cop]