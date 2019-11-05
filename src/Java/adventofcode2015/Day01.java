
package adventofcode2015;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/1
 */
public class Day01 {

    public static void main(String[] args) throws Exception {
        String input = new Input(2015, 1).strings().get(0);

        System.err.println(
            input.chars().reduce(0, (i, b) -> (b == '(') ? i+1 : i-1));

        int depth = 0, i = 0;
        for (; depth != -1; i++) {
            depth += input.charAt(i) == '(' ? 1 : -1;
        }
        System.err.println(i);
    }

}
