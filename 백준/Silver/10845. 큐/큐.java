
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Q q = new Q(N);
        for (int i=0;i<N;i++){
            String[] arr = br.readLine().split(" ");
            if (arr[0].equals("push")){
                q.push(Integer.parseInt(arr[1]));
            } else if (arr[0].equals("pop")){
                System.out.println(q.pop());
            } else if (arr[0].equals("size")){
                System.out.println(q.size());
            } else if (arr[0].equals("empty")){
                System.out.println(q.empty());
            } else if (arr[0].equals("front")){
                System.out.println(q.front());
            } else if (arr[0].equals("back")) {
                System.out.println(q.back());
            }
        }
    }
}

class Q{
    int front;
    int back;
    int[] elem;

    Q(int N){
        this.front = 0;
        this.back = 0;
        this.elem = new int[N];
    }

    void push(int X){
        elem[back] = X;
        this.back++;
    }

    int pop(){
        if (this.size()==0){
            return -1;
        } else{
            this.front++;
            return elem[this.front-1];
        }
    }

    int size(){
        return back-front;
    }

    int empty(){
        return this.size() == 0 ? 1 : 0;
    }

    int front(){
        return back==front ? -1 : elem[front];
    }

    int back(){
        return back==front ? -1 : elem[back-1];
    }


}