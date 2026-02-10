class Solution {
    static String answer = new String();
    static StringBuilder sb;
    public String solution(String new_id) {
        answer = new_id;
        first();
        second();
        third();
        fourth();
        fifth();
        sixth();
        seventh();
        return answer;
    }
    static void first(){
        sb = new StringBuilder();
        for (char c : answer.toCharArray()){
            if (Character.isUpperCase(c)){
                sb.append(Character.toLowerCase(c));
            } else{
                sb.append(c);
            }
        }
        answer = sb.toString();
    }
    
    static void second(){
        sb = new StringBuilder();
        for (char c : answer.toCharArray()){
            if (Character.isLowerCase(c) || Character.isDigit(c) || c=='-' || c=='_' || c=='.'){
                sb.append(c);
            }
        }
        answer = sb.toString();
    }
    
    static void third(){
        sb = new StringBuilder();
        int cnt = 0;
        for (char c : answer.toCharArray()){
            if (c=='.'){
                cnt+=1;
            } else {
                if (cnt>0) {
                    sb.append('.');
                    cnt=0;
                }
                sb.append(c);
            }
        }
        if (cnt>0 && answer.length()>0 && answer.charAt(answer.length()-1)=='.') sb.append('.');
        answer=sb.toString();
    }
    
    static void fourth(){
        
        sb = new StringBuilder(answer);
        if (sb.charAt(0)=='.') sb.deleteCharAt(0);
        if (sb.length()>0 && sb.charAt(sb.length()-1)=='.') sb.deleteCharAt(sb.length()-1);
        answer = sb.toString();
    }
    
    static void fifth(){
        if (answer.length()==0) answer="a";
    }
    
    static void sixth(){
        if (answer.length()>15){
            answer = answer.substring(0,15);
        }
        
        if (answer.charAt(answer.length()-1) == '.'){
            answer = answer.substring(0,14);
        }
    }
    
    static void seventh(){
        sb = new StringBuilder(answer);
        while (sb.length() <3){
            sb.append(answer.charAt(answer.length()-1));
        } 
        answer = sb.toString();
        
    }
    
}