/*
완전 탐색을 돌기에는 50억번 돌게 됨 -> X

*/

import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        Stack<Integer> stack = new Stack<>();  // 인덱스를 저장
        
        for (int i = 0; i < n; i++) {
            // 현재 가격이 stack의 top보다 낮으면 떨어졌다는 뜻
            while (!stack.isEmpty() && prices[stack.peek()] > prices[i]) {
                int topIndex = stack.pop();
                answer[topIndex] = i - topIndex;  // 몇 초 뒤에 떨어졌는지
            }
            stack.push(i);  // 현재 인덱스를 스택에 넣음
        }
        
        // 끝까지 가격이 안 떨어진 경우
        while (!stack.isEmpty()) {
            int topIndex = stack.pop();
            answer[topIndex] = n - 1 - topIndex;
        }
        
        return answer;
    }
}