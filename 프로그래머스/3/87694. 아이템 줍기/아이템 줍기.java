import java.util.*;
class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        int[][] map = new int[102][102];
        for (int[] arr : rectangle){
            int x1 = arr[0]*2, y1 = arr[1]*2;
            int x2 = arr[2]*2, y2 = arr[3]*2;
            for (int i=x1; i<=x2; i++){
                for (int j=y1; j<=y2; j++){
                    if (map[i][j]==2) continue;
                    
                    if (i==x1 || i==x2 || j==y1 || j==y2){
                        if(map[i][j]!=2){
                            map[i][j] = 1;
                        }
                    } else{
                        map[i][j] = 2;
                    }
                }
            }
        }        
        
        int[] dx = new int[]{0,0,-1,1};
        int[] dy = new int[]{1,-1,0,0};
        
        boolean[][] visited = new boolean[102][102];
        Queue<int[]> q = new LinkedList<>(); // {x,y,dist}
        int startX = characterX * 2;
        int startY = characterY * 2;
        int targetX = itemX * 2;
        int targetY = itemY * 2;
        // BFS 사용 최단 거리 구하기 
        q.offer(new int[]{startX,startY,0}); // 초기 위치
        visited[startX][startY] = true;
        
        while(!q.isEmpty()){
            int[] arr = q.poll();
            int x = arr[0];
            int y = arr[1];
            int dist = arr[2];
            
            if (x==targetX && y==targetY){
                return dist/2;
            }
            
            for (int i=0;i<4;i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx <= 100 && ny >= 0 && ny <= 100 && map[nx][ny] == 1 && !visited[nx][ny] ){
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx,ny,dist+1});
                }
            }
        }
        return answer;
    }
}