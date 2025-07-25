/*
그냥 스택 포인트를 사용하면 될듯?
stackPoint -> -1 이면 빈 스택
(가 들어오면 +1, 
)가 들어오면 stackPoint가 -1인지 확인(스택이 비어있나확인)하고 -1 비어있다면 false


*/
class Solution {
    boolean solution(String s) {
        int stackPoint = -1;
        for (int i=0;i<s.length();i++){
          if (s.charAt(i) == '('){
              stackPoint+=1;
          } else{
              if (stackPoint<0){
                  return false;
              } else{
                  stackPoint-=1;
              }
          }
        }
        if (stackPoint==-1){
            return true;
        }else{
            return false;
        }
        
    }
}