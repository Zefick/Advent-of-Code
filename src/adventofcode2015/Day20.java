
package adventofcode2015;

/**
 * https://adventofcode.com/2015/day/20
 */
public class Day20 {

    public static void main(String[] args) {

        int input = 33100000;

        for (int i=1; ; i++) {
            int s = i;
            for (int j=2; j<=Math.sqrt(i); ++j) {
                if (i%j == 0) {
                    int k = (i/j);
                    s += j;
                    if (k != j) s += k;
                }
            }
            if (s*10 >= input) {
                System.err.println(i);
                break;
            }
        }

        for (int i=1; ; i++) {
            int s = 0;
            for (int j=1; j<=Math.sqrt(i); ++j) {
                if (i%j == 0) {
                    int k = (i/j);
                    if (k <= 50) s += j;
                    if (k != j && j<=50) s += k;
                }
            }
            if (s*11 >= input) {
                System.err.println(i);
                break;
            }
        }
    }

}
