
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Member[] members = new Member[N];
        for (int i=0; i<N; i++){
            String[] arr = br.readLine().split(" ");
            Member member = new Member(Integer.parseInt(arr[0]), arr[1]);
            members[i] = member;
        }
        Arrays.sort(members, (a,b) -> a.age-b.age);
        for (int i=0; i<N; i++){
            Member man = members[i];
            System.out.println(man.age + " " + man.name);
        }
    }
}

class Member{
    int age;
    String name;

    Member(int age, String name){
        this.age = age;
        this.name = name;
    }
}