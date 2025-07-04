class Solution {
    public int solution(int n) {
        int answer = 0;
        // 기본적인 완탐
        if (n%2!=0){
            for (int i=1;i<=n;i+=2){
                answer=answer+i;
            }
        } else {
            for (int i=2;i<=n;i+=2){
                answer=answer+i*i;
            }
        }
        
    
        return answer;
    }
}