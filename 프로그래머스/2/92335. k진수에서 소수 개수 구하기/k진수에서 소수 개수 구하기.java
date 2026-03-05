import java.util.*;
class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        // 1. n을 k진법으로 변환한다. 
        String convertN = convert(n,k);
        
        // 2. 변환된 수 convert를 0으로 split한다. 
        String[] arr = convertN.split("0");
        // 3. split된 애들 각각 소수 검사해준다.
        for (String num : arr){
            if (num.equals("") || num.equals("1")) continue;
            long checkNum = Long.parseLong(num);
            if (check(checkNum)){
                answer++;
            }
        }
        return answer;
    }
    String convert(int num, int k){
        StringBuilder sb = new StringBuilder();
        while (num>0){
            sb.append(num%k);
            num/=k;
        }
        return sb.reverse().toString();
    }
    Boolean check(long num){
        for (int i=2; i<=Math.sqrt(num) ; i++){
            if (num%i==0){
                return false;
            }   
        }
        return true;
    }
}