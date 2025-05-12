
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String target = sc.nextLine(); // 공백 포함 입력
        String st = sc.nextLine();     // 찾을 단어
        int answer = 0;

        for (int i = 0; i <= target.length() - st.length(); i++) {
            boolean isMatch = true;
            for (int j = 0; j < st.length(); j++) {
                if (target.charAt(i + j) != st.charAt(j)) {
                    isMatch = false;
                    break;
                }
            }
            if (isMatch) {
                answer++;
                i += st.length() - 1; // 겹치지 않게 건너뛰기
            }
        }

        System.out.println(answer);
    }
}