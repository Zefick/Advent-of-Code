
package adventofcode2016;

import java.util.Comparator;
import java.util.stream.IntStream;

public class Day06 {

    public static void main(String[] args) {
        int dict[][] = new int[8][26];

        Utils.getStringsFromFile("input06.txt").forEach(s -> {
            IntStream.range(0, 8).forEach(i -> dict[i][s.charAt(i)-'a']++);
        });
        // finds least frequent character.
        // 0 transformed to 100
        IntStream.range(0, 8)
            .mapToObj(i -> (char)(IntStream.range(0, 26).boxed()
                    .min(Comparator.comparing(x -> (dict[i][x]-1) % 100)).get()+'a'))
            .forEach(System.out::print);
    }

}
