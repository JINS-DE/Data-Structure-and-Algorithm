/*
1. 숫자를 문자열 배열로 변환
2. 정렬 : a+b, b+a 크기 비교
3. 문자열 합치기
4. "00", "000" 예외 처리 -> 0으로 시작하면 0
*/
import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        // #1
        String[] list = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .toArray(String[]::new);
        
        // #2
        Arrays.sort(list,(a,b)->((b+a).compareTo(a+b)));
        
        // #3
        String answer = String.join("",list);
        
        // #4
        if (answer.startsWith("0")) return "0";
        
        return answer;
    }
}