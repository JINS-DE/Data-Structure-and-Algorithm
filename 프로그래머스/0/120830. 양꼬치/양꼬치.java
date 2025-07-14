class Solution {
    public int solution(int n, int k) {
        return n*12000+2000*((n/10)>=k?0:(k-n/10));
    }
}