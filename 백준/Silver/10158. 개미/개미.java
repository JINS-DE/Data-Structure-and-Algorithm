import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt();
        int h = sc.nextInt();
        int p = sc.nextInt();
        int q = sc.nextInt();
        int t = sc.nextInt();

        int currX = (t+p) % (2*w);
        int currY = (t+q) % (2*h);
        if (currX > w) currX = 2*w -currX;
        if (currY > h) currY = 2*h -currY;

        System.out.println(currX + " " + currY);

    }
}