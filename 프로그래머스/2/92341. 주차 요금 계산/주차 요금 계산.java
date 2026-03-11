import java.util.*;
class Solution {
    public int[] solution(int[] fees, String[] records) {
        Map<String,String> recordHash = new HashMap<>();
        Map<String,Integer> totalTime = new HashMap<>();
        // 1. 각각 차량의 사용 시간 계산하기 (records 순회)
        for (String record : records){
            String[] arr = record.split(" ");
            String time = arr[0];
            String carNum = arr[1];
            String type = arr[2];
            // 1-1. IN일 때 recordHash 추가, Out이면 시간 계산 후 시간 저장(totalTime 저장) 후 recordHash 요소 삭제
            if (type.equals("IN")){
                recordHash.put(carNum,time);
            } else {
                // 시간 계산
                String inTime = recordHash.get(carNum);
                int parkingTime = timeCount(inTime,time);
                totalTime.put(carNum, totalTime.getOrDefault(carNum,0) + parkingTime);
                
                // 요소 삭제
                recordHash.remove(carNum);
            }
        }
        // 1-2. recordHash 남은 애들 23:59 기준으로 일괄 시간 계산 후 hashmap에 저장    
        for (Map.Entry<String,String> entry : recordHash.entrySet()){
            String carNum = entry.getKey();
            String time = entry.getValue();
            totalTime.put(carNum, totalTime.getOrDefault(carNum,0) + timeCount(time,"23:59"));
        }
        
        // 2. 해쉬 keyset 기준으로 정렬된 배열 만들기
        String[] sortedArr = totalTime.keySet().toArray(new String[0]);
        Arrays.sort(sortedArr);
        int carTotalCount = sortedArr.length;
        int[] result = new int[carTotalCount];
        // 3. 정렬된 배열을 순차적으로 순회하며 정산하기
        int basicTime = fees[0];
        int basicFee = fees[1];
        int perTime = fees[2];
        int perPrice = fees[3];
        for (int i=0; i< carTotalCount; i++){
            String carNum = sortedArr[i];
            int total = totalTime.get(carNum);
            if (total <= basicTime){
                result[i] = basicFee;
            } else{
                result[i] = basicFee + (int) Math.ceil((double)(total-basicTime)/perTime) * perPrice;
            }
        }
        return result;
    }
    
    private int timeCount(String in, String out){
        String[] arr1 = in.split(":");
        String[] arr2 = out.split(":");
        int inTime = Integer.parseInt(arr1[0])*60 + Integer.parseInt(arr1[1]);
        int outTime = Integer.parseInt(arr2[0])*60 + Integer.parseInt(arr2[1]);
        return outTime - inTime;
    }
}