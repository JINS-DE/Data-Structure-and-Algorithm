def solution(temperature, t1, t2, a, b, onboard):  
    # 초기값 설정  
    cost = 1000 * 100       # 최댓값 설정(onboard 길이 최댓값 * a,b 최댓값)  
    t1 += 10                # 음수를 제거하기 위해 -10 <= t1, t2 <= 40 을 0 <= t1, t2 <= 50 으로 옮긴다  
    t2 += 10  
    temperature += 10       # t1, t2 도 옮겼으니 temprature 도 + 10 을 해준다  

    # DP[i][j] : i분에 j 온도를 만들 수 있는 가장 적은 전력  
    dp = [[cost] * 51 for _ in range(len(onboard))]  # j = 0 ~ 50  
    dp[0][temperature] = 0  

    flag = 1  # 에어컨을 가동했을 때 온도가 변하는 방향 설정  
    if temperature > t2:  
        flag = -1   # 최적의 온도보다 외부 온도가 높다면  

    for i in range(1, len(onboard)):  
        for j in range(51):  
            ans = [cost]  
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:  
                # 1. 에어컨을 끄고, 실내온도 방향으로 1 변화
                if 0 <= j + flag <= 50:  
                    ans.append(dp[i - 1][j + flag])  
                # 2. 에어컨을 끄고 현재온도 j 가 실외온도랑 같아서 변하지 않는 경우
                if j == temperature:  
                    ans.append(dp[i - 1][j])  
                # 3. 에어컨을 키고 현재온도가 변하는 경우 
                if 0 <= j - flag <= 50:  
                    ans.append(dp[i - 1][j - flag] + a)  
                # 4. 에어컨을 키고 현재온도가 희망온도라서 온도가 변하지 않는경우  
                if t1 <= j <= t2:  
                    ans.append(dp[i - 1][j] + b)  

                dp[i][j] = min(ans)  

    answer = min(dp[len(onboard) - 1])  
    return answer
