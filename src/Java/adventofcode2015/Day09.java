package adventofcode2015;

import java.io.IOException;
import java.util.*;
import java.util.function.Function;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/9
 */
public class Day09 {

    static Map<String, Map<String, Integer>> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        new Input(2015, 9)
                .match("(\\w+) to (\\w+) = (\\d+)")
                .forEach(m -> {
            String from = m.group(1);
            String to = m.group(2);
            Integer dist = Integer.parseInt(m.group(3));
            map.putIfAbsent(from, new HashMap<>());
            map.putIfAbsent(to, new HashMap<>());
            map.get(from).put(to, dist);
            map.get(to).put(from, dist);
        });
        map.keySet().stream()
                .mapToInt(first -> visit(new ArrayDeque<>(), first, IntStream::min))
                .min().ifPresent(System.err::println);

        map.keySet().stream()
                .mapToInt(first -> visit(new ArrayDeque<>(), first, IntStream::max))
                .max().ifPresent(System.err::println);
    }

    static int visit(Deque<String> visited, String current, Function<IntStream, OptionalInt> func) {
        visited.push(current);
        IntStream result = map.keySet().stream()
                .filter(next -> !visited.contains(next))
                .mapToInt(next -> visit(visited, next, func) + map.get(current).get(next));
        visited.pop();
        return func.apply(result).orElse(0);
    }

}
