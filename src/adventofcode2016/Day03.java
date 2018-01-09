
package adventofcode2016;

import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

import utils.Input;

public class Day03 {

    static boolean possible(int a, int b, int c) {
        return (a < b+c) && (b < a+c) && (c < a+b);
    }

    public static void main(String[] args) {
        List<String> lines = new Input(2016, "input03.txt").strings();
        int[] sides = lines.stream()
                .flatMap(x -> Arrays.stream(x.trim().split("\\s+")))
                .mapToInt(Integer::valueOf)
                .toArray();

        long n = IntStream.range(0, lines.size())
                .filter(i -> possible(sides[i*3], sides[i*3+1], sides[i*3+2]))
                .count();

        System.out.println(n);

        n = IntStream.range(0, lines.size())
                .filter(i -> possible(sides[i/3*9 + i%3], sides[i/3*9 + i%3 + 3], sides[i/3*9 + i%3 + 6]))
                .count();

        System.out.println(n);
    }

}
