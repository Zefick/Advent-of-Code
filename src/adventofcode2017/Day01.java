
package adventofcode2017;

import java.util.PrimitiveIterator.OfInt;
import java.util.stream.IntStream;

import utils.Input;

public class Day01 {

    static int calc(String input, int dist) {
        OfInt s2 = IntStream.concat(input.chars(), input.chars()).skip(dist).iterator();
        return input.chars()
                .filter(i -> i == s2.next())
                .map(i -> i - '0')
                .sum();
    }

    public static void main(String[] args) throws Exception {
        String input = new Input(2017, "input01.txt").strings().get(0);
        System.out.println(calc(input, 1));
        System.out.println(calc(input, input.length() / 2));
    }

}
