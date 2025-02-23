import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int X = Integer.parseInt(sc.nextLine());
		String N = sc.nextLine();
		int res = 0;
		for(int i=1; i<=Integer.parseInt(N); i++) {
			String ab = sc.nextLine();
			int a = Integer.parseInt(ab.split(" ")[0]);
			int b = Integer.parseInt(ab.split(" ")[1]);
			res += a*b;
		}
		if(X==res) {
			System.out.println("Yes");
		}else {
			System.out.println("No");
		}
	}
}
