import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int C = sc.nextInt();
        Map<Integer,Integer> freq = new HashMap<>();
        Map<Integer,Integer> idxOrder = new HashMap<>();
        for (int i =0;i<N;i++){
            int inp = sc.nextInt();
            freq.put(inp,freq.getOrDefault(inp,0)+1);
            idxOrder.putIfAbsent(inp,i);
        }
        List<Integer> keys = new ArrayList<>(freq.keySet());

        keys.sort((o1,o2)->{
            int a = freq.get(o1);
            int b = freq.get(o2);
            if (a!=b) return b-a;
            return idxOrder.get(o1) - idxOrder.get(o2);
        });

        StringBuilder sb  = new StringBuilder();
        for (int num: keys){
            int count = freq.get(num);
            for (int i = 0; i < count; i++) {
                sb.append(num+ " ");
            }
        }
        System.out.println(sb.toString());
    }
}