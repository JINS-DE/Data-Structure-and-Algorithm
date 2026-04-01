import java.util.*;

class Solution {
    public String solution(String number, int k) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char current : number.toCharArray()) {
            
            // 앞에 작은 숫자 제거
            while (!stack.isEmpty() && k > 0 && stack.peekLast() < current) {
                stack.pollLast();
                k--;
            }
            
            stack.offerLast(current);
        }
        
        // k가 남아있으면 뒤에서 제거
        while (k > 0) {
            stack.pollLast();
            k--;
        }
        
        // 결과 만들기
        StringBuilder result = new StringBuilder();
        for (char c : stack) {
            result.append(c);
        }
        
        return result.toString();
    }
}