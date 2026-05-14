/*
1순위 : 재생의 합이 가장 큰 장르부터 
2순위 : 장르에서 많이 재생된 노래
        - 재생 횟수가 같으면 고유 번호가 낮은 노래가 우선 순위
        
출력 : 베스트 노래의 고유 번호 순대로 배열 출력
*/

import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 0-1. 2개의 해쉬 선언 ("장르": "총 재생수", "장르":"index 목록" )
        Map<String, Integer> playCount = new HashMap<>();
        Map<String, List<Integer>> genrePK = new HashMap<>();
        // 0-2. genreNames : 장르의 이름들 모음 list 선언
        List<String> genreNames = new ArrayList<>();
        // 0-3. answer 선언
        List<Integer> answer = new ArrayList<>();
        
        // 0-4. 데이터 입력
        for (int i=0; i<genres.length;i++){
            String genre = genres[i];
            Integer cnt = plays[i];
            // 총 재생수 갱신
            playCount.put(genre, playCount.getOrDefault(genre,0) + cnt);
            
            // index 추가 
            List<Integer> indexList;
            if(genrePK.get(genre)==null){
                indexList = new ArrayList<>();
            } else{
                indexList = genrePK.get(genre);
            };
            indexList.add(i);
            genrePK.put(genre,indexList);
        }
        
        // 1. 장르 총 재생수 별로 장르 정렬 
        // 1-1. genreNames 초기화
        for (String name : playCount.keySet()){
            genreNames.add(name);
        }
        
        // 1-2. genreNames 각 장르별 총 재생수로 이름 정렬 
        Collections.sort(genreNames,(o1,o2)->playCount.get(o2) - playCount.get(o1));
        
        // 2. genreNames 순회하면서 "장르":"index 목록"해쉬의 index 목록 정렬 후 앞에 두 개만 가져와서 answer 추가
        for (String genre : genreNames){
            List<Integer> arr = genrePK.get(genre);
            Collections.sort(arr,(o1,o2)->plays[o2] - plays[o1]);
            for (int i=0 ; i < ((arr.size()<2)?1:2); i++){
                answer.add(arr.get(i));
            }
        }
        
        // 3. answer (ArrayList -> int[] )
        int[] result = new int[answer.size()];
        for (int i=0; i<answer.size();i++){
            result[i] = answer.get(i);
        }
        
        return result;
    }
}