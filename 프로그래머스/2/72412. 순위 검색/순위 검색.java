/*
1. hash 만들기 
- query조합:[해당 점수 리스트]
Map<String,List<Integer>> hash = new HashMap<>(); 
- info에서 가능한 모든 경우의 수 hash에 삽입 

2. List<Integer> 오름차순 정렬
3. 쿼리 순회 하면서 리스트에 바이너리 서치로 low-bound 찾기
- cnt += 쿼리 전체 크기 - 해당 인덱스

*/

import java.util.*;
class Solution {
    public int[] solution(String[] info, String[] query) {
        int[] result = new int[query.length];
        // 1. hash 만들기 
        Map<String,List<Integer>> hash = new HashMap<>(); 
        for (String s : info){
            String[] user = s.split(" ");
            String[] langes = {user[0],"-"};
            String[] jobs = {user[1],"-"};
            String[] careers = {user[2],"-"};
            String[] foods = {user[3],"-"};
            int score = Integer.parseInt(user[4]);
            
            for (String lang : langes){
                for (String job : jobs){
                    for (String career : careers){
                        for (String food : foods){
                            String key = lang + job + career + food;
                            List<Integer> arr = hash.getOrDefault(key,new ArrayList<Integer>());
                            arr.add(score);
                            hash.put(key,arr);
                        }
                    }
                }
            }
        }
        
        // 2. 점수 리스트 오름차순 정렬
        for (String key : hash.keySet()){
            Collections.sort(hash.get(key));
        }
        // 3. 쿼리 순회
        for (int i=0; i<query.length;i++){
            String str = query[i].replace(" and ","");
            String[] parts = str.split(" ");
            String qKey = parts[0];
            int qScore = Integer.parseInt(parts[1]);
            
            if (hash.containsKey(qKey)){
                List<Integer> arr = hash.get(qKey);
                // 전체크기 - 바이너리 서치로 low-bound 찾기
                result[i] = arr.size() - binarySearch(arr, qScore);
            } else {
                result[i] = 0;
            }
            
        }
        
        
        
        return result;
        
    }
    int binarySearch(List<Integer> arr, int val){
        int left = 0;
        int right = arr.size();

        while (left<right){
            int mid = (left+right)/2;
            if (arr.get(mid) >= val){
                right = mid;
            } else{
                left = mid + 1;
            }
        }
        return left;
    }
    
}