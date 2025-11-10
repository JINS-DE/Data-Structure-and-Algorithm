import java.util.*;
import java.io.*;

public class Main{
    static int[] nums;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        nums = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        // N 크기 배열 채우기
        for (int i=0;i<N;i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);
        // 테스트 케이스 M개 test
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        // test 크기 배열 채우기
        for (int i=0;i<M;i++){
            int num = Integer.parseInt(st.nextToken());
            bw.write((binarySearch(num)?"1\n":"0\n"));
        }
        bw.flush();

    }

    public static boolean binarySearch(int target){
        int mid;
        int left = 0;
        int right = nums.length - 1;
        while (left<=right){
            mid = (left+right)/2;
            if (nums[mid] > target ){
                right = mid-1;
            } else if (nums[mid] < target){
                left = mid+1;
            } else {
                return true;
            }
        }
        return false;
    }
}