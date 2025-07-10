class Solution {
    static String[] map = new String[5];
    // 좌,하,우
    static int[] dr = {0,1,0};
    static int[] dc = {-1,0,1};
    static int[] answer = new int [5];
    static int [][] visited=new int[5][5];
    
    public int[] solution(String[][] places) {
        for (int i=0;i<5;i++){
            map = places[i];
            visited=new int[5][5];
            if(isRightDistance()){
                answer[i]=1;
            }
        }
        return answer;
    }
    
    
    static boolean isRightDistance(){
        for (int i=0;i<5;i++){
            for(int j=0;j<5;j++){
                if (map[i].charAt(j)=='P'){
                    visited[i][j]=1;
                    if(check(i,j)){
                        for (int k = 0; k<3;k++){
                            int nr = i+dr[k];
                            int nc = j+dc[k];
                            
                            if( nr>=0 && nr<5 && nc>=0 && nc<5 && visited[nr][nc]==0) {
                                if(!check(nr,nc))return false;
                            }
                            
                    }    
                    } else {
                        return false;
                    }
                }
                    
            }
        }
        return true;
    }
    static boolean check(int i, int j){
        if (map[i].charAt(j)=='X') return true;
        for (int k = 0; k<3;k++){
            int nr = i+dr[k];
            int nc = j+dc[k];
            
            if( nr>=0 && nr<5 && nc>=0 && nc<5){
                if (visited[nr][nc]==0 && map[nr].charAt(nc)=='P') return false;
            }
        }
        return true;
        
    }
}