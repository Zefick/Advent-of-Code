
package adventofcode2015;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.IntSupplier;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/13
 */
public class Day13 {

    static int calc(List<Integer> members, int mas[][]) {
        IntSupplier shuffle = () -> {
            Collections.shuffle(members);
            int x = 0;
            for (int j=0; j<members.size(); ++j) {
                int a = members.get(j);
                int b = members.get((j+1) % members.size());
                x += mas[a][b] + mas[b][a];
            }
            return x;
        };
        return IntStream.generate(shuffle).limit(100000).max().getAsInt();
    }

    public static void main(String[] args) {
        int mas[][] = new int[9][9];
        List<String> chars = Arrays.asList("ABCDEFGM".split(""));
        new Input(2015, 13)
                .match("([A-Z]).*(gain|lose) (\\d+).*([A-Z])")
                .forEach(m -> {
            int n = Integer.parseInt(m.group(3));
            mas[chars.indexOf(m.group(1))][chars.indexOf(m.group(4))]
                    = m.group(2).equals("gain") ? n : -n;
        });
        System.err.println(calc(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7), mas));
        System.err.println(calc(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8), mas));
    }

}
