import java.util.*;
class Solution {
    static Map<Integer,int[]> keypad;
    static int leftPosition;
    static int rightPosition;
    static boolean direct; // 왼손잡이 true, 오른손잡이 false
    
    public String solution(int[] numbers, String hand) {
        // 초기화
        direct = hand.equals("left") ? true : false;
        
        keypad = new HashMap<>();
        int key = 1;
        for (int i=0;i<4;i++){
            for(int j=0;j<3;j++){
                keypad.put(key++,new int[]{i,j});
            }
        }
        keypad.put(0,new int[]{3,1});
        leftPosition = 10;
        rightPosition = 12;
        
        Set<Integer> onlyLeft = new HashSet<>(Arrays.asList(1,4,7));
        Set<Integer> onlyRight = new HashSet<>(Arrays.asList(3,6,9));
        StringBuilder result = new StringBuilder();
        
        for (int number : numbers){
            if (onlyLeft.contains(number)){
                result.append('L');
            } else if(onlyRight.contains(number)){
                result.append('R');
            } else{
                int distLeft;
                int distRight;
                distLeft = Math.abs(keypad.get(number)[0]-keypad.get(leftPosition)[0]) + 
                    Math.abs(keypad.get(number)[1]-keypad.get(leftPosition)[1]);
                
                distRight = Math.abs(keypad.get(number)[0]-keypad.get(rightPosition)[0]) + 
                    Math.abs(keypad.get(number)[1]-keypad.get(rightPosition)[1]);
                
                if (distLeft-distRight > 0){
                    result.append("R");
                } else if (distLeft-distRight < 0){
                    result.append("L");
                } else{
                    result.append(direct ? "L" : "R");
                }
            }
            // 이동
            if (result.charAt(result.length()-1) == 'L'){
                leftPosition = number;
            } else{
                rightPosition = number;
            }
        }
        
        return result.toString();
    }
    
}