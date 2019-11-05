
package adventofcode2017;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.IntStream;

/**
 * https://adventofcode.com/2017/day/6
 */
public class Day06 {

    public static void main(String[] args) throws Exception {
        int banks[] = {14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4};
        int cycles = 0;
        boolean firstloop = true;

        Set<Integer> hashes = new HashSet<>();
        for (;;) {
            cycles++;
            int j = IntStream.range(1, banks.length)
                    .reduce(0, (a, b) -> banks[a] >= banks[b] ? a : b);

            int n = banks[j];
            banks[j] = 0;
            for (; n>0; n--) {
                banks[++j%16]++;
            }
            int hash = Arrays.hashCode(banks);
            if (hashes.contains(hash)) {
                if (firstloop) {
                    hashes.clear();
                    firstloop = false;
                    System.out.println(cycles);
                    cycles = 0;
                } else {
                    break;
                }
            }
            hashes.add(hash);
        }
        System.out.println(cycles);
    }

}
