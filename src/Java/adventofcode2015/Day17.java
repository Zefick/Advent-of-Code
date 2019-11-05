
package adventofcode2015;

import java.util.TreeMap;

/**
 * https://adventofcode.com/2015/day/17
 */
public class Day17 {

    public static void main(String[] args) {

        int containers[] = {43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38};

        TreeMap<Integer, Integer> combinations = new TreeMap<>();

        for (int i=0; i<(1<<20); ++i) {
            int sum = 0;
            for (int j=0; j<20; ++j) {
                sum += ((i & (1<<j)) > 0) ? containers[j] : 0;
            }
            if (sum == 150) {
                int n = Integer.bitCount(i);
                combinations.put(n, combinations.getOrDefault(n, 0) + 1);
            }
        }
        System.out.println(combinations);
        System.err.println(combinations.values().stream().mapToInt(Integer::intValue).sum());
        System.err.println(combinations.firstEntry().getValue());
    }

}
