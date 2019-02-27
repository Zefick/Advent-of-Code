
package adventofcode2015;

import java.util.List;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/5
 */
public class Day05 {

    public static void main(String[] args) {
        List<String> input = new Input(2015, 5).strings();

        long n1 = input.stream()
                .filter(str -> str.matches(".*[aeiou].*[aeiou].*[aeiou].*"))
                .filter(str -> str.matches(".*(.)\\1.*"))
                .filter(str -> !str.matches(".*(ab|cd|pq|xy).*"))
                .count();
        System.err.println(n1);

        long n2 = input.stream()
                .filter(str -> str.matches(".*(..).*\\1.*"))
                .filter(str -> str.matches(".*(.).\\1.*"))
                .count();
        System.err.println(n2);
    }

}
