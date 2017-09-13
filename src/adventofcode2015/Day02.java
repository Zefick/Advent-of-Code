
package adventofcode2015;

import java.util.Arrays;
import java.util.List;
import java.util.function.ToIntFunction;

import utils.Input;

public class Day02 {

    private static int handle(String present, ToIntFunction<int[]> func) {
        int dims[] =  Arrays.stream(present.split("x"))
                .mapToInt(Integer::parseInt).sorted().toArray();
        return func.applyAsInt(dims);
    }

    private static int wrap(int[] dims) {
        int a = dims[0] * dims[1], b = dims[1] * dims[2], c = dims[2] * dims[0];
        return 2 * (a+b+c) + a;
    }

    private static int ribbon(int[] dims) {
        return 2 * (dims[0] + dims[1]) + dims[0] * dims[1] * dims[2];
    }

    public static void main(String[] args) {
        List<String> input = new Input(2015, "input02.txt").strings();
        // part 1
        System.out.println("paper: " +
                input.stream().mapToInt(p -> handle(p, Day02::wrap)).sum());
        // part 2
        System.out.println("ribbon: " +
                input.stream().mapToInt(p -> handle(p, Day02::ribbon)).sum());
    }

}
