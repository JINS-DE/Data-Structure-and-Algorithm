import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for (int i=0;i<T;i++){
            int input = Integer.parseInt(br.readLine());
            boolean flag = false;
            for (int j=2; j<=64; j++){
                String st = convertBase(input,j);
                StringBuffer s = new StringBuffer(st);
                if (st.equals(s.reverse().toString())){
                    flag = true;
                    break;
                }
            }
            if (!flag){
                bw.write('0' );
                bw.write('\n' );
            } else{
                bw.write('1');
                bw.write('\n');
            }
            bw.flush();

        }
    }
    public static String convertBase(int n, int base){
        StringBuffer sb = new StringBuffer();
        while (n>0){
            int mod = n%base;
            if (mod < 10){
                sb.append(mod);
            } else {
                sb.append((char) ('A' + (mod - 10)));
            }
            n/=base;
        }

        return sb.reverse().toString();

    }
}