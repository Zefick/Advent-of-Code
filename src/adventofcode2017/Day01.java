
package adventofcode2017;

import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2017/day/1
 */
public class Day01 {

    static int calc(String input, int dist) {
        int[] chars = input.chars().map(i -> i - '0').toArray();
        int n = chars.length;
        return IntStream.range(0, n)
                .map(i -> chars[i] == chars[(i+dist)%n] ? chars[i] : 0)
                .sum();
    }

    public static void main(String[] args) throws Exception {
        String input = new Input(2017, 1).strings().get(0);
        System.out.println(calc(input, 1));
        System.out.println(calc(input, input.length() / 2));
    }

}
