
package adventofcode2015;

public class Day20 {

    public static void main(String[] args) {

        int input = 33100000;

        for (int i=1; ; i++) {
            int s = 0;
            for (int j=1; j<=Math.sqrt(i); ++j) {
                if (i%j == 0) {
                    int k = (i/j);
                    if (k <= 50) s += j;
                    if (k != j && j<=50) s += k;
                }
            }
            System.out.println(i + " - " + s*11);
            if (s*11 >= input) {
                System.out.println(i);
                break;
            }
        }
    }

}
