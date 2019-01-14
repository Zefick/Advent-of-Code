
package adventofcode2017;

import java.util.Arrays;
import java.util.List;
import java.util.function.IntFunction;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import utils.Input;

/**
 * https://adventofcode.com/2017/day/13
 */
public class Day13 {

    public static void main(String[] args) throws Exception {
        List<int[]> firewall = new Input(2017, 13).strings().stream()
                .map(s -> Arrays.stream(s.split(": ")).mapToInt(Integer::parseInt).toArray())
                .collect(Collectors.toList());

        IntFunction<Stream<int[]>> func = delay -> firewall.stream()
                .filter(x -> (x[0] + delay) % ((x[1]-1)*2) == 0);

        System.out.println(func.apply(0).mapToInt(x -> x[0] * x[1]).sum());

        IntStream.iterate(0, i -> i+1)
                .filter(i -> !func.apply(i).findFirst().isPresent())
                .limit(1).forEach(System.out::println);
    }
}
