

import java.util.Scanner;
import java.util.Stack;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String pipe = sc.nextLine();
		Stack<Character> stack = new Stack<Character>();
		int answer=0;
		for(int i=0;i<pipe.length();i++){
			if (pipe.charAt(i) == '('){
				stack.push('(');
			} else{
				if(pipe.charAt(i-1)=='('){
					stack.pop();
					answer+=stack.size();
				} else{
					stack.pop();
					answer+=1;
				}
			}
		}
		System.out.println(answer);
	}
}
