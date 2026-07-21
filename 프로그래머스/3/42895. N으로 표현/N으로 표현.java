import java.util.*;
class Solution {
    public int solution(int N, int number) {
        Set<Integer> [] sets = new Set[9];
        
        // set 초기화
        for (int i=1;i<=8;i++){
            sets[i] = new HashSet<>();
        }
        
        // 최소값이 8보다 크면 -1 return 조건으로 인한 8까지 수행
        for (int i=1; i<=8; i++){
            sets[i].add(makeSequenceNum(N,i));
            
            for(int j=1;j<i;j++){
                Set<Integer> a = sets[j];
                Set<Integer> b = sets[i-j];
                for (int num1 : a){
                    for (int num2 : b){
                        sets[i].add(num1+num2);
                        sets[i].add(num1*num2);
                        sets[i].add(num1-num2);
                        
                        if (num2!=0){
                            sets[i].add(num1/num2);
                        }
                    }
                }
            }
            if (sets[i].contains(number)){
                return i; 
            }
            
        }
        return -1;
    }
    private int makeSequenceNum(int n, int cnt){
        int result = 0;
        for (int i=0; i<cnt; i++){
            result = result*10 + n;
        }
        return result;
    }
}