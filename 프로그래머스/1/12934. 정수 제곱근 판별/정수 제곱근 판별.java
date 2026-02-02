class Solution {
    public long solution(long n) {
        long left = 1;
        // 핵심 수정: n이 아무리 커도 제곱근은 3,037,000,499를 넘을 수 없습니다.
        // 불필요한 큰 수 계산을 막아 오버플로우를 방지합니다.
        long right = Math.min(n, 3037000499L); 

        while (left <= right) {
            long mid = left + (right - left) / 2;
            long pow = mid * mid; 

            if (pow == n) {
                return (mid + 1) * (mid + 1);
            } else if (pow < n) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}