import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String now = sc.nextLine();
		String target = sc.nextLine();
		String[] nowTime = now.split(":");
		int nTime = Integer.parseInt(nowTime[0])*3600 + Integer.parseInt(nowTime[1])*60 +Integer.parseInt(nowTime[2]);

		String[] targetTime = target.split(":");
		int tTime = Integer.parseInt(targetTime[0])*3600 + Integer.parseInt(targetTime[1])*60 +Integer.parseInt(targetTime[2]);
		
		int answer = tTime -nTime;
		if(answer <= 0) {
			answer+=24*3600;
		}

		int answerHour = answer/3600;
		int answerMinute = (answer%3600)/60;
		int answerSecond = (answer%3600)%60;

		System.out.printf("%02d:%02d:%02d",answerHour,answerMinute,answerSecond);

	}
}