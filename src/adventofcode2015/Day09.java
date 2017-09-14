package adventofcode2015;

import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day09 {

    static Map<String, Map<String, Integer>> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        List<String> input = new Input(2015, "input09.txt").strings();
        Pattern p = Pattern.compile("(\\w+) to (\\w+) = (\\d+)");
        for (String s : input) {
            Matcher m = p.matcher(s);
            m.find();
            String from = m.group(1);
            String to = m.group(2);
            Integer dist = Integer.parseInt(m.group(3));
            map.putIfAbsent(from, new HashMap<>());
            map.putIfAbsent(to, new HashMap<>());
            map.get(from).put(to, dist);
            map.get(to).put(from, dist);
        }
        map.keySet().stream()
                .mapToInt(first -> visit(new ArrayDeque<>(), first))
                .max().ifPresent(System.out::println);
    }

    static int visit(Deque<String> visited, String current) {
        visited.push(current);
        int max = map.keySet().stream()
            .filter(next -> !visited.contains(next))
            .mapToInt(next -> visit(visited, next) + map.get(current).get(next))
            .max().orElse(0);
        visited.pop();
        return max;
    }

}
