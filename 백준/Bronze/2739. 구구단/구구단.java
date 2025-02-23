import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String v = sc.nextLine();
		for(int i=1; i<10; i++) {
			System.out.println(v+" * "+i+" = "+Integer.parseInt(v)*i);
		}
	}
}
