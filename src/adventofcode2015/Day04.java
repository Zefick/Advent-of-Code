
package adventofcode2015;

import java.util.stream.IntStream;

import utils.MD5;

/**
 * https://adventofcode.com/2015/day/4
 */
public class Day04 {

    static int find(String input, String prefix) {
        return IntStream.iterate(1, x -> x+1)
                .filter(x -> MD5.encode(input + x).startsWith(prefix))
                .findFirst().getAsInt();
    }

    public static void main(String[] args) {
        String input = "ckczppom";
        System.err.println(find(input, "00000"));
        System.err.println(find(input, "000000"));
    }

}
