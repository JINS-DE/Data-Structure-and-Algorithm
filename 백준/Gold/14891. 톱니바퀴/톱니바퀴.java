import java.io.*;
import java.util.*;
public class Main {
    static int K;
    static int[][] cycle;
    static int[] pointer = new int[5];
    static boolean[] isSame = new boolean[5];
    static String[] wheel = new String[5];
    public static void main(String[] args) throws IOException {
        input();
        for (int i=0; i<K;i++){
            int num = cycle[i][0];
            // 시계방향 true, 반시계방향 false
            boolean rotation = cycle[i][1] == 1;


            boolean direct = rotation;
            rotate(num,direct);
            // 왼쪽 확인
            for (int j=num-1; j>=1; j--){
                if (isSame[j]) break;
                rotate(j,!direct);
                direct = !direct;
            }
            direct = rotation;
            // 오른쪽 확인
            for (int j=num; j<4; j++){
                if (isSame[j]) break;
                rotate(j+1,!direct);
                direct = !direct;
            }

            initStatus();
        }
        int answer = 0;
        for (int i=1; i<5;i++){
            if (wheel[i].charAt(pointer[i]) == '1'){
                answer += 1<<(i-1);
            }
        }
        System.out.println(answer);
    }
    static void rotate(int num, boolean direct){
        if (direct){
            pointer[num] = (pointer[num] +7) % 8;
        } else{
            pointer[num] = (pointer[num] +1) % 8;
        }
    }

    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i=1;i<=4;i++){
            wheel[i] = br.readLine();
        }

        initStatus();
        K = Integer.parseInt(br.readLine());
        cycle = new int[K][2];
        for (int i=0; i<K; i++){
            String[] arr = br.readLine().split(" ");
            cycle[i][0] = Integer.parseInt(arr[0]);
            cycle[i][1] = Integer.parseInt(arr[1]);
        }
    }
    static void initStatus(){
        for (int i=1;i<4;i++){
            String wheelA = wheel[i];
            String wheelB = wheel[i+1];
            int pointA = pointer[i];
            int pointB = pointer[i+1];
            isSame[i] = wheelA.charAt((pointA + 2) % 8) == wheelB.charAt((pointB - 2 + 8) % 8);
        }
    }
}

