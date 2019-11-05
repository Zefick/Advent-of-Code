package adventofcode2018;

/**
 * https://adventofcode.com/2018/day/11
 */
public class Day11 {

    static void findMax(int input, int s1, int s2) {
        int max = -1000000;
        int maxx = 0, maxy = 0, maxs = 0;
        for (int size = s1; size<=s2; size++) {
            for (int i=1; i<=298; i++) {
                for (int j=1; j<=298; j++) {
                    int s = Math.min(size, Math.min(301-i, 301-j));
                    int power = 0;
                    for (int x = 0; x<s; ++x) {
                        for (int y = 0; y<s; ++y) {
                            int rackID = (i+x) + 10;
                            int p = (rackID * (y+j) + input) * rackID;
                            power += (p/100) % 10 - 5;
                        }
                    }
                    if (max < power) {
                        max = power;
                        maxx = i;
                        maxy = j;
                        maxs = s;
                    }
                }
            }
        }
        if (s1 == s2) {
            System.err.printf("%d,%d %d\n", maxx, maxy, max);
        } else {
            System.err.printf("%d,%d,%d %d\n", maxx, maxy, maxs, max);
        }
    }

    public static void main(String[] args) {
        int input = 3613;
        findMax(input, 3, 3);
        findMax(input, 1, 30);
    }

}
