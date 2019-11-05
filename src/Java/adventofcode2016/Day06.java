
package adventofcode2016;

import java.util.List;
import java.util.stream.IntStream;

import utils.Input;
import utils.Utils;

/**
 * https://adventofcode.com/2016/day/6
 */
public class Day06 {

    public static void main(String[] args) {
        int dict[][] = new int[8][26];

        List<String> strings = new Input(2016, 6).strings();
        strings.forEach(s -> IntStream.range(0, 8)
                .forEach(i -> dict[i][s.charAt(i)-'a']++));

        IntStream.range(0, 8)
                .mapToObj(i -> (char)(Utils.maxIndex(dict[i])+'a'))
                .forEach(System.err::print);
        System.err.println();

        IntStream.range(0, 8)
                .mapToObj(i -> (char)(Utils.minIndex(dict[i])+'a'))
                .forEach(System.err::print);
    }

}
