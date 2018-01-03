
package adventofcode2017;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import utils.Input;

public class Day24 {

    public static void main(String[] args) {
        List<String> input = new Input(2017, "input24.txt").strings();

        List<int[]> parts = new ArrayList<>();

        for (String s : input) {
            String ss[] = s.split("/");
            parts.add(new int[] {Integer.parseInt(ss[0]), Integer.parseInt(ss[1])});
        }

        Deque<Integer> q = new ArrayDeque<>();
        Set<Integer> used = new HashSet<>();
        int i = 0;
        int max[] = {0, 0}, maxlen = 0;
        int count = 0;
        int head = 0;

        while (true) {
            if (i == parts.size()) {
                count++;
                int val = q.stream().mapToInt(j -> parts.get(j)[0] + parts.get(j)[1]).sum();
                max[0] = Math.max(max[0], val);
                if (q.size() >= maxlen) {
                    max[1] = Math.max(max[1], val);
                    maxlen = q.size();
                }
                i = q.pop() + 1;
                used.remove(i-1);
                head = head == parts.get(i-1)[0] ? parts.get(i-1)[1] : parts.get(i-1)[0];
                if (q.isEmpty()) {
                    break;
                }
                continue;
            }
            if (!used.contains(i) && parts.get(i)[0] == head) {
                q.push(i);
                used.add(i);
                head = parts.get(i)[1];
                i = 0;
            } else if (!used.contains(i) && parts.get(i)[1] == head) {
                q.push(i);
                used.add(i);
                head = parts.get(i)[0];
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
