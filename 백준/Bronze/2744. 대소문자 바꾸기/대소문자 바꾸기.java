import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String word = br.readLine();
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < word.length(); i++) {
            char w = word.charAt(i);
            if (Character.isUpperCase(w)) {
                answer.append(Character.toLowerCase(w));
            } else {
                answer.append(Character.toUpperCase(w));
            }
        }
        System.out.println(answer);
    }}