
package adventofcode2017;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

import utils.Input;

public class Day12 {

    public static void main(String[] args) throws Exception {
        List<String> input = new Input(2017, "input12.txt").strings();

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
