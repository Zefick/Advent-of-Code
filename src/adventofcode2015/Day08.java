
package adventofcode2015;

import java.util.List;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/8
 */
public class Day08 {

    public static void main(String[] args) {
        List<String> input = new Input(2015, 8).strings();

        int n = input.stream()
                .mapToInt(s -> s.length() - s.replaceAll("\\\\\\\\|\\\\\"|\\\\x..", "_").length() + 2)
                .sum();
        System.out.println(n);

        n = input.stream()
                .mapToInt(s -> s.replaceAll("\\\\|\"", "__").length() - s.length() + 2)
                .sum();
        System.out.println(n);
    }

}
