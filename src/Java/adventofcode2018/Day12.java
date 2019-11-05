package adventofcode2018;

import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/12
 */
public class Day12 {

    public static void main(String[] args) {
        String state =".....##.####..####...#.####..##.#..##..#####.##.#..#...#.###.###....####.###...##..#...##.#.#...##.##";
        Set<String> notes = new Input(2018, 12)
                .strings().stream()
                .map(s -> s.split(" => "))
                .filter(rule -> rule[1].equals("#"))
                .map(rule -> rule[0])
                .collect(Collectors.toSet());

        for (int i=1; i<10000; i++) {
            String prevState = state;
            String newState = "..." + state + "....";
            state = IntStream.range(0, newState.length()-4)
                    .mapToObj(n -> newState.substring(n, n+5))
                    .map(s -> notes.contains(s) ? "#" : ".")
                    .collect(Collectors.joining())
                    .substring(1)
                    .replaceFirst("\\.*$", "");
            if (i == 20) {
                System.err.println(count(state));
            }
            if (state.equals("." + prevState)) {
                int n = state.replace(".", "").length();
                System.err.println((50_000_000_000L - i) * n + count(state));
                break;
            }
        }
    }

    static int count(String s) {
        return IntStream.range(0, s.length())
                .filter(i -> s.charAt(i) == '#')
                .map(i -> i-5)
                .sum();
    }

}
