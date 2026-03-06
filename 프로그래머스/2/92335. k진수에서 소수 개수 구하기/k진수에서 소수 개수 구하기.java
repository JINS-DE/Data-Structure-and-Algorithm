import java.util.*;
class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        // 1. n을 k진법으로 변환한다. 
        String convertN = Integer.toString(n,k);
        // 2. 변환된 수 convert를 0으로 split한다. 
        String[] arr = convertN.split("0+");
        // 3. split된 애들 각각 소수 검사해준다.
        for (String num : arr){
            if (isPrime(Long.parseLong(num))){
                answer++;
            }
        }
        return answer;
    }
    
    private boolean isPrime(long n){
        if (n<2) return false;
        if (n==2) return true;
        if (n%2==0) return false;
        
        for (long i=3;i*i<=n;i=i+2){
            if (n%i==0) return false;
        }
        return true;
    }
}