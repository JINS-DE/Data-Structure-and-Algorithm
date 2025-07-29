/*
초기 세팅
1. bridge_length 길이 만큼의 queue 생성 및 0으로 초기화
2. queue 안에 총 무게를 갱신해줄 변수 now_weight = 0 으로 초기화

풀이
 !q.isEmpty()까지 while문
1. 매 시간마다 q.poll() 
2. now_weight가 weight보다 작고 추가적 다리에 올라갈 수 있는 무게가 되면 q에 추가
*/

import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> q = new LinkedList<>();
        for (int i=0;i<bridge_length;i++){
            q.offer(0);    
        }
        int time=0;
        int now_weight=0;
        int idx = 0;
        int size = truck_weights.length;
        while (!q.isEmpty()){
            time++;
            now_weight-=q.poll();
            if (idx < size){
                int offerWeight = truck_weights[idx];
                if (now_weight+offerWeight<=weight){
                    q.offer(offerWeight);
                    now_weight += offerWeight;
                    idx++;
                } else{
                    q.offer(0);
                }
            }
        }
        return time;
    }
}