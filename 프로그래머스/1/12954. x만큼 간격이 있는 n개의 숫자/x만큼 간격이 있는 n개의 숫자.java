class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long v = x;
        for (int i=0;i<n;i++){
            answer[i] = v;
            v+=x;
        }
        
        return answer;
    }
}