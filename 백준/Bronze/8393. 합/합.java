import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String v = sc.nextLine();
		int res = 0;
		for(int i=1; i<Integer.parseInt(v)+1; i++) {
			res += i;
		}
		System.out.println(res);
	}
}
