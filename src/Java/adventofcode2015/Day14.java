
package adventofcode2015;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/14
 */
public class Day14 {

    public static void main(String[] args) {
        List<int[]> stats = new Input(2015, 14)
                .match("(\\d+).*?(\\d+).*?(\\d+)")
                .map(m -> IntStream.range(1, 4)
                        .map(i -> Integer.parseInt(m.group(i)))
                        .toArray())
                .collect(Collectors.toList());
        int n = stats.size();
        int d[] = new int[n];
        int scores[] = new int[n];
        for (int t=1; t<=2503; ++t) {
            for (int j=0; j<n; ++j) {
                int stat[] = stats.get(j);
                int period = stat[1] + stat[2];
                d[j] = (t/period*stat[1] + Math.min(stat[1], t%period)) * stat[0];
            }
            int max = IntStream.of(d).max().getAsInt();
            IntStream.range(0, n)
                    .filter(x -> d[x] == max)
                    .forEach(x -> scores[x]++);
        }
        System.err.println(IntStream.of(d).max().getAsInt());
        System.err.println(IntStream.of(scores).max().getAsInt());
    }

}
