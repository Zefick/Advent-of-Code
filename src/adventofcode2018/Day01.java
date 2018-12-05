package adventofcode2018;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/1
 */
public class Day01 {

    public static void main(String[] args) {

        int[] numbers = new Input(2018, "input01.txt")
                .strings().stream()
                .mapToInt(Integer::parseInt)
                .toArray();

        System.err.println(Arrays.stream(numbers).sum());

        int result = 0;
        Set<Integer> reached = new HashSet<>(Collections.singleton(0));
        for (int i=0; ; i++) {
            result += numbers[i % numbers.length];
            if (reached.contains(result)) break;
            reached.add(result);
        }
        System.err.println(result);
    }

}
