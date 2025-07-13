class Solution {
    public int[][] solution(int[][] arr) {
        int rowSize = arr.length;
        int colSize = arr[0].length;

        // 행과 열이 같으면 그대로 반환
        if (rowSize == colSize) {
            return arr;
        }

        int size = Math.max(rowSize, colSize);
        int[][] answer = new int[size][size];

        // 원본 복사
        for (int i = 0; i < rowSize; i++) {
            for (int j = 0; j < colSize; j++) {
                answer[i][j] = arr[i][j];
            }
        }

        return answer;
    }
}
