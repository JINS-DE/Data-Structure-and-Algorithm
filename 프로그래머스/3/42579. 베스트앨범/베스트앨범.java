/*
# 여기서 배운 java 문법
- hash
    .computeIfAbsent('key', k->new ArrayList<>())
    .add()
- map.entrySet()는 파이썬에서 dic.items()랑 같음
- map.Entry<type,type> -> key : value  나타내기

# 자료구조 : 해쉬
- 장르별 총 재생횟수 저장 해쉬  Map<String,Integer>
- 장르별 각 재생횟수 리스트 해쉬 Map<String,ArrayList<int[]>> -> 재생 횟수 뿐만 아니라 고유번호도 저장해야함

# 로직 흐름
1. 각 해쉬들 정보 넣기
2. totalPlayHash value 크기 별로 내림차순 정렬
3. 정렬된 totalPlayHash에서 순서대로 key를 뽑고 key를 통해 playListHash의 value를 정렬한다.
4. 해당 ArrayList 정렬 0번째 : index, 1번째 : 크기 -> 크기 별로 정렬, 다음 index 오름차순  
*/
import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        Map<String,Integer> totalPlayHash = new HashMap<>();
        Map<String, ArrayList<int[]>> playListHash = new HashMap<>();
        
        for (int i=0; i<genres.length;i++){
            totalPlayHash
                .put(genres[i],totalPlayHash.getOrDefault(genres[i],0)+plays[i]);
            
            playListHash
                .computeIfAbsent(genres[i], k -> new ArrayList<>())
                .add(new int[]{i, plays[i]});
        }
        
        List<Map.Entry<String,Integer>> list = new ArrayList<>(totalPlayHash.entrySet());
        
        list.sort((a,b)->b.getValue() - a.getValue());
          
        List<Integer> answerList = new ArrayList<>();
    
         for (Map.Entry<String, Integer> dic : list) {
            String genre = dic.getKey();
            ArrayList<int[]> songs = playListHash.get(genre);

            // 곡 정렬: 재생수 ↓, 인덱스 ↑
            songs.sort((a, b) -> {
                if (b[1] != a[1]) return b[1] - a[1];
                return a[0] - b[0];
            });

            // 1등 곡 추가
            answerList.add(songs.get(0)[0]);

            // 2등 곡 있으면 추가
            if (songs.size() >= 2) {
                answerList.add(songs.get(1)[0]);
            }
        }
        
        return  answerList.stream().mapToInt(i -> i).toArray();
    }
}