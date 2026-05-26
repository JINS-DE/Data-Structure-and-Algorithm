import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        // 초기화
        Queue<int[]> q = new LinkedList<>();
        int n = maps.length;
        int m = maps[0].length;
        int[] dr = new int[]{1,-1,0,0};
        int[] dc = new int[]{0,0,-1,1};
        
        boolean flag = false;
        // 방문 = 2
        int answer=1;
        maps[0][0] = 2;
        q.offer(new int[]{0,0,1});
        while (!q.isEmpty()){
            int[] arr = q.poll();
            int r = arr[0];
            int c = arr[1];
            int depth = arr[2];
            if (r==n-1 && c==m-1){
                flag = true;
                answer = depth;
                break;
            }
            
            for (int i=0; i<4; i++){
                int nr = dr[i] + r;
                int nc = dc[i] + c;
                if (nr>=0 && nr < n && nc>=0 && nc < m && maps[nr][nc]!=0 && maps[nr][nc]!=2){
                    q.offer(new int[]{nr,nc,depth+1});
                    maps[nr][nc] = 2;
                }
            }
            
        }
        return flag?answer:-1;
    }
}