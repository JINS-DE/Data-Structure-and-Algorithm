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
        answer = answer.replaceAll("[^a-z0-9_.-]","");
    }
    static void third(){
        answer = answer.replaceAll("\\.+",".");
    }
    static void fourth(){
        answer = answer.replaceAll("^[.]|[.]$","");
    }
    static void fifth(){
        if (answer.length() == 0){
            answer = "a";
        }
    }
    static void sixth(){
        if (answer.length()>15){
            answer = answer.substring(0,15);
        }
        answer = answer.replaceAll("\\.$","");
    }
    static void seventh(){
        int strSize = answer.length();
        char lastChar = answer.charAt(strSize-1);
        while (strSize<3){
            answer += lastChar;
            strSize = answer.length();
        }
    }
    
}