
package adventofcode2015;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/15
 */
public class Day15 {

    public static void main(String[] args) {
        List<int[]> stats = new Input(2015, 15)
                .match("([-0-9]+).*?([-0-9]+).*?([-0-9]+).*?([-0-9]+).*?([-0-9]+)")
                .map(m -> IntStream.range(1, 6)
                        .map(i -> Integer.parseInt(m.group(i)))
                        .toArray())
                .collect(Collectors.toList());
        int max1 = 0, max2 = 0;
        for (int i1=0; i1<=100; ++i1) {
            for (int i2=i1; i2<=100; ++i2) {
                for (int i3=i2; i3<=100; ++i3) {
                    int parts[] = {i1, i2 - i1, i3 - i2, 100 - i3};
                    int scores[] = IntStream.range(0, 5)
                            .map(n -> IntStream.range(0, 4).map(x -> stats.get(x)[n]*parts[x]).sum())
                            .map(x -> Math.max(0, x))
                            .toArray();
                    int result = scores[0] * scores[1] * scores[2] * scores[3];
                    if (scores[4] == 500) {
                        max2 = Math.max(result, max2);
                    }
                    max1 = Math.max(result, max1);
                }
            }
        }
        System.err.println(max1);
        System.err.println(max2);
    }

}
