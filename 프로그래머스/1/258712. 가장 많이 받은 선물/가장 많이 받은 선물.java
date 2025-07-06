/* 문제 풀이
1. friends 총 개수 = n 이라면 n*n 2차원 배열 만들기 -> 선물 개수 갱신 
2. friends의 각 index 별로 hash 저장 (ex)"muzi":0, "ryan":1 
3. 선물 지수용 hash -> 선물 받으면 -1 주면 +1
4. gifts 돌면서 "선물개수","선물지수" 갱신
5. 2중 for문을 돌면서 각각 받을 선물 개수 구하면서 max값 갱신하기. Default max=0
*/

import java.util.*;
class Solution {
    public int solution(String[] friends, String[] gifts) {
        int n = friends.length;
        // 1번
        int[][] presentCountArray = new int[n][n];
        
        // 2번
        Map<String,Integer> friendIndex = new HashMap<>();
        for (int i=0;i<n;i++){
           friendIndex.put(friends[i],i);
        }
        
        // 3번
        Map<String,Integer> friendsDegree = new HashMap<>();
        
        // 4번
        for (int i=0; i<gifts.length;i++){
            String[] tmp = gifts[i].split(" ");
            String giver = tmp[0];
            String given = tmp[1];
            presentCountArray[friendIndex.get(giver)][friendIndex.get(given)]+=1;
            friendsDegree.put(giver,friendsDegree.getOrDefault(giver,0)+1);
            friendsDegree.put(given,friendsDegree.getOrDefault(given,0)-1);
        }
        int[] answer = new int[n];
        // 5번
        for (int i=0; i<n-1;i++){
            for(int j=i+1; j<n;j++){
                int tmp;
                if (presentCountArray[i][j] > presentCountArray[j][i]){
                    answer[i]+=1;
                }else if((presentCountArray[i][j] < presentCountArray[j][i])){
                    answer[j]+=1;
                }else{
                    int degreeI = friendsDegree.getOrDefault(friends[i],0);
                    int degreeJ = friendsDegree.getOrDefault(friends[j],0);
                    if (degreeI > degreeJ){
                        answer[i]+=1;
                    } else if(degreeI<degreeJ){
                        answer[j]+=1;
                    }
                    
                }
            }
        }
        
        return Arrays.stream(answer).max().getAsInt();
    }
}