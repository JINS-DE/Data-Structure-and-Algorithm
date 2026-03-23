
import java.io.*;
import java.util.*;
public class Main {
    static String alpha;
    public static void main(String[] args) throws IOException{
        input();
        String[] arr = {"c=","c-","dz=","d-","lj","nj","s=","z="};
        for (String st : arr){
            alpha = alpha.replace(st,"!");
        }
        System.out.println(alpha.length());
    }



    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        alpha = br.readLine();
    }
}
