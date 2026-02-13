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
        // 1. hash 만들기
        Map<String,ArrayList<Integer>> hash = new HashMap<>();
        makeHash(info,hash);
        
        // 2. 해쉬 value 리스트 정렬하기
        for (String key : hash.keySet()){
            Collections.sort(hash.get(key));
        }
        // 3. 쿼리 순회하면서 해쉬 value 리스트에서 이진탐색으로 target 찾기
        int[] result = new int[query.length];
        int i = 0;
        for (String q : query){
            String[] qList = q.replace(" and ", "").split(" ");
            String qKey = qList[0];
            int qScore = Integer.parseInt(qList[1]);
            if (hash.containsKey(qKey)) {
                ArrayList<Integer> scoreList = hash.get(qKey);
                result[i] = scoreList.size() - binarySearch(scoreList, qScore);
            } else {
                result[i] = 0;
            }
            
            i++;
        }
        
        
        return result;
    }
    
    private int binarySearch(ArrayList<Integer> arr, int target){
        int left = 0;
        int right = arr.size();
        while (left<right){
            int mid = (left+right)/2;
            if (arr.get(mid) < target){
                left = mid + 1;
            } else{
                right = mid;
            }
        }
        return left; 
        
    }
    
    
    private void makeHash(String[] info, Map<String,ArrayList<Integer>> hash ){
        for (String s : info){
            String[] user = s.split(" ");
            String[][] options = {
                {user[0],"-"}, {user[1],"-"}, {user[2],"-"}, {user[3],"-"}
            };
            int score = Integer.parseInt(user[4]);
            
            generateCombinations(0,"",options, hash,score);
        }
    }
    
    private void generateCombinations(int depth, String key, String[][] options, Map<String,ArrayList<Integer>> hash,int score){
        if (depth==4){
            if (hash.containsKey(key)){
                hash.get(key).add(score);
            } else{
                ArrayList<Integer> list = new ArrayList<>();
                list.add(score);
                hash.put(key,list);
            }
            return;
        }
        
        generateCombinations(depth+1, key + options[depth][0], options, hash, score);
        generateCombinations(depth+1, key + options[depth][1], options, hash, score);
    }
}