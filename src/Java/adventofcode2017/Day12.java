
package adventofcode2017;

import java.util.*;
import java.util.stream.Collectors;

import utils.Input;

/**
 * https://adventofcode.com/2017/day/12
 */
public class Day12 {

    public static void main(String[] args) throws Exception {
        List<String> input = new Input(2017, 12).strings();
        Map<String, Set<String>> groups = new HashMap<>();

        for (String s : input) {
            Set<String> group = Arrays.stream(s.split("( <-> )|(, )"))
                    .flatMap(id -> groups.getOrDefault(id, Collections.singleton(id)).stream())
                    .collect(Collectors.toSet());
            group.forEach(id -> groups.put(id, group));
        }

        System.out.println(groups.get("0").size());
        System.out.println(groups.values().stream().distinct().count());
    }
}
