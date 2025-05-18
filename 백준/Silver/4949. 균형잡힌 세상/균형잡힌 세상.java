

import java.util.Scanner;

public class Main {
    static boolean isMatch(char open, char close){
        if (open == '(' && close ==')')
            return true;
        if (open == '[' && close == ']')
            return true;
        return false;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()){
            char[] line = sc.nextLine().toCharArray();
            if (line.length == 1 && line[0] == '.')
                break;

            char[] stack = new char[line.length];
            int top = -1;
            boolean isValid = true;
            for (char ch : line){
                if (ch == '(' || ch=='['){
                    stack[++top] = ch;
                } else if (ch==')' || ch==']'){
                    if (top < 0 || !isMatch(stack[top--],ch)){
                        isValid = false;
                        break;
                    }

                }
            }
            if (top>=0) isValid = false;
            System.out.println(isValid ? "yes":"no");

        }
    }
}
