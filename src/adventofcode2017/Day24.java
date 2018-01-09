
package adventofcode2017;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import utils.Input;

public class Day24 {

    public static void main(String[] args) {
        List<String> input = new Input(2017, "input24.txt").strings();

        List<int[]> parts = input.stream()
                .map(s -> s.split("/"))
                .map(s -> new int[] {Integer.parseInt(s[0]), Integer.parseInt(s[1])})
                .collect(Collectors.toList());

        Deque<Integer> bridge = new ArrayDeque<>();
        Set<Integer> used = new HashSet<>();
        int i = 0;
        int max[] = {0, 0}, maxlen = 0;
        int count = 0;
        int head = 0;

        while (true) {
            if (i == parts.size()) {
                count++;
                int val = bridge.stream().map(parts::get).mapToInt(p -> p[0] + p[1]).sum();
                max[0] = Math.max(max[0], val);
                if (bridge.size() >= maxlen) {
                    max[1] = Math.max(max[1], val);
                    maxlen = bridge.size();
                }
                i = bridge.pop();
                if (bridge.isEmpty()) {
                    break;
                }
                used.remove(i);
                head = parts.get(i)[1] + parts.get(i)[0] - head;
                i++;
            } else if (!used.contains(i) && (parts.get(i)[0] == head || parts.get(i)[1] == head)) {
                bridge.push(i);
                used.add(i);
                head = parts.get(i)[1] + parts.get(i)[0] - head;
                i = 0;
            } else {
                i++;
            }
        }
        System.out.println(count);
        System.out.println(max[0]);
        System.out.println(max[1]);
    }
}
