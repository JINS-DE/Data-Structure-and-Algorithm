class Solution {
    public long solution(long n) {
        long root = (long) Math.sqrt(n);
        if (root*root==n){
            return (root+1)*(root+1);
        }
        return -1;
    }
}