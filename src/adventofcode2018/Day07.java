package adventofcode2018;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.TreeSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/7
 */
public class Day07 {

    static Pattern p = Pattern.compile("Step (.) must be finished before step (.) can begin.");

    public static void main(String[] args) {

        Map<String, List<String>> order = new HashMap<>();
        Set<String> steps = new TreeSet<>();

        List<String> input = new Input(2018, "input07.txt").strings();
        for (String s : input) {
            Matcher m = p.matcher(s);
            m.find();
            String s1 = m.group(1);
            String s2 = m.group(2);
            steps.add(s1);
            steps.add(s2);
            List<String> list;
            if (order.containsKey(s2)) {
                list = order.get(s2);
            } else {
                list = new ArrayList<>();
                order.put(s2, list);
            }
            list.add(s1);
        }
        order.values().stream().forEach(list -> list.sort(Comparator.naturalOrder()));
        System.out.println(order);

        /*
        while (!steps.isEmpty()) {
            String first = steps.stream()
                    .filter(s -> !order.containsKey(s) || order.get(s).isEmpty())
                    .findFirst().get();
            steps.remove(first);
            System.err.print(first);
            order.values().stream().forEach(list -> list.remove(first));
        }
        //*/

        int n = 5;
        int time = 0;
        int workers[] = new int[n];
        String letters[] = new String[n];
        while (!order.isEmpty()) {
            time++;
            for (int i=0; i<n; i++) {
                workers[i] = Math.max(0, workers[i]-1);
            }
            for (int i=0; i<n; i++) {
                if (workers[i] == 0 && letters[i] != null) {
                    String l = letters[i];
                    order.values().stream().forEach(list -> list.remove(l));
                    order.remove(l);
                    letters[i] = null;
                }
            }
            for (int i=0; i<n; i++) {
                if (workers[i] == 0) {
                    Optional<String> first = steps.stream()
                            .filter(s -> !order.containsKey(s) || order.get(s).isEmpty())
                            .findFirst();
                    int ii = i;
                    first.ifPresent(l -> {
                        steps.remove(l);
                        workers[ii] = l.codePointAt(0) - 'A' + 61;
                        letters[ii] = l;
                    });
                }
            }
        }
        System.err.println(time - 1);
    }

}
