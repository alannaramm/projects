
public class Ascii_Tree {

    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            // Print leading spaces
            for (int j = 10; j > i; j--) {
                System.out.print(" ");
            }

            // Print left slashes
            for (int A = 1; A < i; A++) {
                System.out.print("\\");
            }

            // Print trunk
            System.out.print("|");

            // Print right slashes
            for (int H = 1; H < i; H++) {
                System.out.print("/");
            }

            // Move to the next line
            System.out.println();
        }
    }
}

		
		
		
		
		
		
	}

}
