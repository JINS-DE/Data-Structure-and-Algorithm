import java.util.*;
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i=0; i<n;i++){
            String binary = Integer.toBinaryString(arr1[i]|arr2[i]);
            while (n > binary.length()){
                binary = "0" + binary;
            }
            System.out.println(binary);
            binary = binary.replace("1","#");
            binary = binary.replace("0"," ");
            answer[i] = binary;
        }
        
        
        return answer;
    }
}