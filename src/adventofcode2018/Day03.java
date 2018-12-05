package adventofcode2018;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/3
 */
public class Day03 {
    
    static Pattern p = Pattern.compile("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)");
    static byte[][] fabric = new byte[1000][1000];
    
    public static void main(String[] args) {
        List<String> input = new Input(2018, "input03.txt").strings();
        check(0, input);
    }

    static void check(int k, List<String> input) {
        if (k == input.size()) {
            long n = IntStream.range(0, 1000)
                    .flatMap(i -> IntStream.range(0, 1000)
                    .filter(j -> fabric[i][j] > 1))
                    .count();
            System.err.println(n);
            return;
        }
        Matcher m = p.matcher(input.get(k));
        m.find();
        int x = Integer.parseInt(m.group(2));
        int y = Integer.parseInt(m.group(3));
        int w = Integer.parseInt(m.group(4));
        int h = Integer.parseInt(m.group(5));
        IntStream.range(x, x+w)
                .forEach(i -> IntStream.range(y, y+h)
                .forEach(j -> fabric[i][j]++));
        check(k+1, input);

        boolean overlap = IntStream.range(x, x+w)
                .flatMap(i -> IntStream.range(y, y+h).map(j -> fabric[i][j]))
                .allMatch(z -> z == 1);
        if (overlap) System.err.println(Integer.parseInt(m.group(1)));
    }

}
