package adventofcode2016;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

import utils.Input;

/**
 * https://adventofcode.com/2016/day/20
 */
public class Day20 {

    public static void main(String[] args) {

        // collect ranges from input
        List<long[]> ranges = new Input(2016, 20).strings().stream()
                .map(s -> Arrays.stream(s.split("-")).mapToLong(Long::parseLong).toArray())
                .collect(Collectors.toList());

        // finding free ends
        long ends[] = ranges.stream()
                .flatMapToLong(x -> LongStream.of(x[0] - 1, x[1] + 1))
                .filter(x  -> ranges.stream().noneMatch(y -> y[0] <= x &&  x <= y[1]))
                .sorted().toArray();

        System.err.println("lowest: " + ends[1]);

        // calculate the number of allowed numbers
        long allowed = IntStream.range(0, ends.length / 2 - 1)
                .mapToLong(i -> ends[i * 2 + 2] - ends[i * 2 + 1] + 1)
                .sum();
        System.err.println("allowed: " + allowed);
    }

}
