import java.io.*;
import java.util.*;
public class Main {
    static int N,M,K;
    static int[][] land ;
    static int[][] A;
    static List<Tree> deadTrees = new ArrayList<>();
    static Deque<Tree> trees = new ArrayDeque<>();
    public static void main(String[] args) throws IOException{
        input();
        // K년 순환
        for (int i=0;i<K;i++){
            spring();
            summer();
            fall();
            winter();
        }
        int answer = trees.size();
        System.out.println(answer);
    }

    /*
    - 각 칸의 여러개의 나무가 있다면 나이가 어린 나무부터 양분을 먹는다.
    - 나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가한다.
    - 땅에 양분이 부족하면 양분을 못 먹은 나무는 죽는다.
    * */
    static void spring(){
        Deque<Tree> growthTrees = new ArrayDeque<>();

        while(!trees.isEmpty()){
            Tree tree = trees.pollFirst();
            int x = tree.x;
            int y = tree.y;
            int age = tree.age;

            if (land[x][y] >= age){
                land[x][y] -= age;
                tree.age ++;
                growthTrees.addLast(tree);
            } else{
                tree.age/=2;
                deadTrees.add(tree);
            }
        }
        trees = growthTrees;
    }
    // 봄에 죽은 나무가 각 칸에 양분이 추가 된다.
    static void summer(){
        for (Tree deadtree : deadTrees){
            land[deadtree.x][deadtree.y] += deadtree.age;
        }
        deadTrees = new ArrayList<>();
    }
    // 번식 기간이다. 번식하는 나무는 나이가 5의 배수여야 하고, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
    static void fall(){
        int[] dr = {-1,-1,-1,0,0,1,1,1};
        int[] dc = {-1,0,1,-1,1,-1,0,1};
        int[][] tmp = new int[N+1][N+1];
        for (Tree tree : trees){
            int x = tree.x;
            int y = tree.y;
            int age = tree.age;
            if (age%5==0){
                for (int i=0;i<8;i++){
                    int nr = x + dr[i];
                    int nc = y + dc[i];
                    if (nr>0 && nc>0 && nr<=N && nc<=N){
                        tmp[nr][nc]++;
                    }
                }
            }
        }
        for (int i=1;i<=N;i++){
            for (int j=1;j<=N;j++){
                int cnt = tmp[i][j];
                for (int k=0; k<cnt;k++){
                    trees.addFirst(new Tree(i,j,1));
                }
            }
        }
    }

    // 각 칸에 A[r][c] 만큼 양분이 추가 된다.
    static void winter(){
        for (int i=1;i<=N;i++){
            for (int j=1;j<=N;j++){
                land[i][j] += A[i][j];
            }
        }
    }


    static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split(" ");
        N = Integer.parseInt(arr[0]);
        M = Integer.parseInt(arr[1]);
        K = Integer.parseInt(arr[2]);
        land  = new int[N+1][N+1];
        A = new int[N+1][N+1];
        for (int i=1; i<=N; i++){
            String[] tmp = br.readLine().split(" ");
            for (int j=1; j<=N; j++){
                land [i][j] = 5;
                A[i][j] = Integer.parseInt(tmp[j-1]);
            }
        }

        List<Tree> tmpList = new ArrayList<>();
        for (int i=0;i<M;i++){
            String[] tmp = br.readLine().split(" ");
            int x = Integer.parseInt(tmp[0]);
            int y = Integer.parseInt(tmp[1]);
            int z = Integer.parseInt(tmp[2]);
            tmpList.add(new Tree(x,y,z));
        }
        Collections.sort(tmpList);
        for (Tree tree : tmpList){
            trees.addLast(tree);
        }
    }
}
class Tree implements Comparable<Tree>{
    int x;
    int y;
    int age;

    Tree (int x,int y, int age){
        this.x = x;
        this.y = y;
        this.age = age;
    }

    @Override
    public int compareTo(Tree other){
        return this.age - other.age;
    }
}