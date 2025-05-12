import java.util.Scanner;

public class Main {
    public static int [] getCountArray(String st){
        int [] count = new int[26];
        for(int i=0;i<st.length();i++){
            char tmp = st.charAt(i);
            if('a'<= tmp && tmp <='z'){
                count[tmp-'a']++ ;
            } else{
                count[tmp-'A']++;
            }
        }

        return count;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int [] count = getCountArray(str);
        int maxValue = -1;
        char maxAlpha = '?';

        for (int i=0; i<26;i++){
            if(count[i] > maxValue){
                maxValue = count[i];
                maxAlpha = (char)('A'+i);
            } else if (maxValue == count[i]) {
                maxAlpha = '?';
            }
        }
        System.out.print(maxAlpha);
    }
}