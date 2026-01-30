/*
1. 1,4,7 일 때 Left 추가, 3,6,9일 때 Right 추가 후 바뀐 손가락 위치 업데이트
2. 그 외에는 가까운 손가락
2-1. 현재 keypad의 위치와 left와 right 위치를 비교한다.
2-2. 가까운 손가락 result 추가후, 변경 손가락 위치 업데이트

변수 : isLeft - 왼손잡이인가? / leftPos, rigthPos - 왼손,오른손 엄지 현위치 / lDist, rDist 왼,오른 거리
getPos 함수 : 현재 좌표 위치 반환
dist 함수 : 멘헤튼 거리 반환
*/

class Solution {
    public String solution(int[] numbers, String hand) {
        boolean isLeft = hand.equals("left");
        StringBuilder result = new StringBuilder();
        int[] leftPos = new int[]{3,0};
        int[] rightPos = new int[]{3,2};
        
        for (int num : numbers){
            if (num==1 || num==4 || num ==7){
                result.append("L");
                leftPos = getPos(num);
            } else if( num==3 || num==6 || num==9){
                result.append("R");
                rightPos = getPos(num);
            } else{
                int[] target = getPos(num);
                int lDist = dist(leftPos,target);
                int rDist = dist(rightPos,target);
                if (lDist>rDist){
                    result.append("R");
                    rightPos = target;
                } else if (lDist<rDist){
                    result.append("L");
                    leftPos = target;
                } else{
                    if (isLeft){
                        result.append("L");
                        leftPos = target;
                    } else{
                        result.append("R");
                        rightPos = target;
                    }
                }
            }
        }
        return result.toString();
    }
    
    private int[] getPos(int n){
        if (n==0) return new int[]{3,1};
        return new int[]{(n-1)/3,(n-1)%3};
    }
    private int dist(int[] a, int[] b){
        return Math.abs(a[0]-b[0]) + Math.abs(a[1]-b[1]);
    }
}