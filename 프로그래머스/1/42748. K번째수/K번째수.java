import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int n = 0;
        for (int[] command : commands){
            n ++;
        } 
        int[] answer = new int[n];
        for (int i=0; i<n; i++){
            int[] command = commands[i];
            int s = command[0];
            int e = command[1];
            int k = command[2];
            // 1. array 자른 배열 복사
            int[] arr = copyArray(array,s,e);
        
            // 2. 자른 배열 정렬
            Arrays.sort(arr);
        
            // 3. k번째 수 구하기    
            answer[i] = arr[k-1];
        }
        
        return answer;
    }
    private int[] copyArray(int[] arr, int s, int e){
        int[] newArr = new int[e-s+1];
        int idx = 0;
        for (int i = s-1 ; i<e; i++){
            newArr[idx] = arr[i];
            idx++;
        }
        return newArr;
    }
}