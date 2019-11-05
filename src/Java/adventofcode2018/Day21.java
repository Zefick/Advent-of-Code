package adventofcode2018;

import java.util.HashSet;
import java.util.Set;

/**
 * https://adventofcode.com/2018/day/21
 */
public class Day21 {

    public static void main(String[] args) throws Exception {
        int R4 = 0, R5 = 0;
        Set<Integer> visited = new HashSet<>();
        int R4prev = 0;
        for (;;) {
            // line 6
            R5 = R4 | 0x10000;
            R4 = 1765573;
            // line 8
            for (;;) {
                R4 += R5 & 255;
                R4 = ((R4 & 0xFFFFFF) * 65899) & 0xFFFFFF;
                if (R5 < 256) break;
                R5 /= 256;
            }
            // line 29
            if (visited.contains(R4)) {
                System.err.println(R4prev);
                break;
            } else {
                if (visited.isEmpty()) {
                    System.err.println(R4);
                }
                visited.add(R4);
            }
            R4prev = R4;
        }
    }
}
