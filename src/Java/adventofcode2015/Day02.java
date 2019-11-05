
package adventofcode2015;

import java.util.Arrays;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/2
 */
public class Day02 {

    private static int wrap(int[] dims) {
        int a = dims[0] * dims[1], b = dims[1] * dims[2], c = dims[2] * dims[0];
        return 2 * (a+b+c) + a;
    }

    private static int ribbon(int[] dims) {
        return 2 * (dims[0] + dims[1]) + dims[0] * dims[1] * dims[2];
    }

    public static void main(String[] args) {
        int[][] dimensions = new Input(2015, 2)
                .strings().stream()
                .map(s -> Arrays.stream(s.split("x"))
                        .mapToInt(Integer::parseInt).sorted().toArray())
                .toArray(int[][]::new);

        System.err.println("paper: " +
                Arrays.stream(dimensions).mapToInt(Day02::wrap).sum());

        System.err.println("ribbon: " +
                Arrays.stream(dimensions).mapToInt(Day02::ribbon).sum());
    }

}
