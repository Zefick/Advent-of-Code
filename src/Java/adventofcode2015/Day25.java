package adventofcode2015;

/**
 * https://adventofcode.com/2015/day/25
 */
public class Day25 {

    public static void main(String[] args) {
        long n = 20151125;
        int x = 1, y = 1;
        while (y != 2978 || x != 3083) {
            n = (n * 252533) % 33554393;
            if (y == 1) {
                y = x+1;
                x = 1;
            } else {
                ++x;
                --y;
            }
        }
        System.out.println(n);
    }

}
