
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();  // 테스트 케이스 수

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int[] arr = new int[n + 1];
            boolean[] visited = new boolean[n + 1];

            // 1부터 n까지 순열 입력
            for (int j = 1; j <= n; j++) {
                arr[j] = sc.nextInt();
            }

            int count = 0; // 사이클 개수 카운트
            for (int j = 1; j <= n; j++) {
                if (!visited[j]) {
                    bfs(arr, visited, j);
                    count++;
                }
            }

            System.out.println(count);
        }
    }

    static void bfs(int[] arr, boolean[] visited, int start) {
        Queue<Integer> q = new Queue<>(arr.length);
        q.push(start);
        visited[start] = true;

        while (!q.isEmpty()) {
            int now = q.pop();
            int next = arr[now];

            if (!visited[next]) {
                visited[next] = true;
                q.push(next);
            }
        }
    }
}

class Queue<T>{
    int front;
    int rear;
    Object [] q;
    // 원형 큐로 구현
    // 1. push는 rear가 한 칸씩 뒤로
    // 2. pop은 front가 한 칸 뒤로
    // 3. full 상태는 front == (rear+1)%capacity 상태
    // 4. empty 상태는?? front == rear
    Queue(int size){
        this.front = 0;
        this.rear = 0;
        this.q = new Object[size+1];
    }
    void push(T e){
        if (isFull()){
            throw new IllegalStateException("Queue is Full");
        }
        this.q[rear] = e;
        this.rear = (rear+1)%q.length;
    }
    T pop(){
        if (isEmpty()){
            throw new IllegalStateException("Queue is empty");
        }
        T e = (T) q[front];
        this.front = (front+1)%q.length;
        return e;
    }
    Boolean isFull(){
        return (rear+1)%q.length == front;

    }

    Boolean isEmpty(){
        return rear==front;
    }


}