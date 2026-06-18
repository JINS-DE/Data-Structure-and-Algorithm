class Solution {
    char[] alpha = new char[]{'A','E','I','O','U'};
    String target;
    int count=0;
    int ans;
    boolean flag = false;
    public int solution(String word) {
        target = word;
        dfs("");
        
        return ans;
    }
    
    public void dfs(String w){
        if (flag || w.length() > 5 ){
            return;
        }
        
        if (w.equals(target)){
            ans = count;
            flag = true;
            return;
        }
        count++;
        for (char a : alpha){
            dfs(w+a);
        }
    }
    
}