package adventofcode2016;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * https://adventofcode.com/2016/day/19
 */
public class Day19 {

    /**
     * List of fixed capacity blocks.
     */
    static class BlockList {

        List<List<Integer>> blocks;

        BlockList(int N, int s) {
            blocks = IntStream.range(0, N/s+1).mapToObj(j ->
                    IntStream.range(0, s).mapToObj(x -> x + j*s + 1)
                        .collect(Collectors.toList()))
                    .collect(Collectors.toList());
        }

        Integer get (int n, boolean remove) {
            int k = 0;
            for (List<Integer> m : blocks) {
                if (n - k < m.size()) {
                    return remove
                            ? m.remove(n-k)
                            : m.get(n-k);
                }
                k += m.size();
            }
            return null;
        }
    }

    public static void main(String[] args) {
        for (int k=0; k<2; k++) {
            int n = 3017957;
            BlockList m = new BlockList(n, 10000);
            for (int i=0; n > 1; n--) {
                i %= n;
                int j = ((k == 0) ? (i+1) : (i+n/2)) % n;
                m.get(j, true);
                if (i < j) i++;
                if (n % 1000000 == 0) System.out.println(n);
            }
            System.err.println(m.get(0, false));
        }
    }

}
