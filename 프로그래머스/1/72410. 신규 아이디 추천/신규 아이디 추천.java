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
        answer = answer.toLowerCase();
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
        while(answer.indexOf("..")!=-1){
            answer = answer.replace("..",".");
        }
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