class Solution {
    boolean solution(String s) {
        int p=0, y=0;
        s= s.toLowerCase();
        for (char c : s.toCharArray()){
            if (c=='p'){
                p++;
            } else if ( c=='y'){
                y++;
            }
        }
        return p==y;
    }
}