package adventofcode2018;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/25
 */
public class Day25 {

    public static void main(String[] args) throws Exception {
        List<int[]> points = new Input(2018, 25)
                .match("(.+),(.+),(.+),(.+)")
                .map(m -> IntStream.range(0, 4)
                        .map(i -> Integer.parseInt(m.group(i+1)))
                        .toArray())
                .collect(Collectors.toList());

        List<List<int[]>> groups = new ArrayList<>();
        for (int[] star : points) {
            List<int[]> group = null;
            for (List<int[]> g : groups) {
                if (g.stream().anyMatch(s -> Math.abs(star[0] - s[0]) + Math.abs(star[1] - s[1])
                            + Math.abs(star[2] - s[2]) + Math.abs(star[3] - s[3]) <= 3)) {
                    if (group == null) {
                        group = g;
                    } else {
                        group.addAll(g);
                        g.clear();
                    }
                }
            }
            if (group == null) {
                groups.add(new ArrayList<>(Collections.singleton(star)));
            } else {
                group.add(star);
            }
        }
        System.err.println(groups.stream().filter(c -> !c.isEmpty()).count());
    }
}
