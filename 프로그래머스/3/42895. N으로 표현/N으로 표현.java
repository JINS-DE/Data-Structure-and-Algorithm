/*
# cnt=1
5

# cnt = 2
55, 5+5, 5-5, 5*5, 5/5
-> NN + (cnt1 op cnt1)

# cnt = 3
-> NNN + (cnt1 op cnt2) + (cnt2 op cnt1)

# cnt = 4
-> NNNN + (cnt1 op cnt3) + (cnt2 op cnt2) + (cnt3 op cnt1)
*/
import java.util.*;
class Solution {
    public int solution(int N, int number) {
        Set<Integer>[] sets = new Set[9];
        for (int i=1;i<=8;i++){
            sets[i] = new HashSet<>();
        }
        
        for (int cnt=1; cnt<=8; cnt++){
            sets[cnt].add(getSequenceNumber(N,cnt));
            for (int i=1; i<cnt; i++){
                Set<Integer> a = sets[i];
                Set<Integer> b = sets[cnt-i];
                
                for (int n1 : a){
                    for (int n2 : b){
                        sets[cnt].add(n1+n2);
                        sets[cnt].add(n1-n2);
                        sets[cnt].add(n1*n2);
                        if (n2!=0){
                            sets[cnt].add(n1/n2);    
                        }
                    }
                }
            }
            if (sets[cnt].contains(number)){
                return cnt;
            }
        }
        
        
        return -1;
    }
    
    private int getSequenceNumber(int num,int cnt){
        // cnt = 1 -> 5
        // cnt = 2 -> 55
        // cnt = 3 -> 555
        
        StringBuilder sb = new StringBuilder();
        for (int i=0;i<cnt;i++){
            sb.append(num);
        }
        return Integer.parseInt(sb.toString());
    }
}