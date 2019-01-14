package adventofcode2018;

import java.util.Arrays;
import java.util.Calendar;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import adventofcode2018.Day04.Entry.Action;
import utils.Input;
import utils.Utils;

/**
 * https://adventofcode.com/2018/day/4
 */
public class Day04 {

    static class Entry {
        int guard;
        Action action;
        Calendar time;

        enum Action {
            SHIFT, FALL, WAKE_UP;
        }

        Entry(Matcher m) {
            time = Calendar.getInstance();
            time.set(Integer.parseInt(m.group(1)), Integer.parseInt(m.group(2)), Integer.parseInt(m.group(3)), 
                    Integer.parseInt(m.group(4)), Integer.parseInt(m.group(5)));
            if (m.group(7) != null) {
                guard = Integer.parseInt(m.group(8));
                action = Action.SHIFT;
            } else if (m.group(9) != null) {
                action = Action.FALL;
            } else {
                action = Action.WAKE_UP;
            }
        }
    }

    public static void main(String[] args) {
        String regexp = "\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2})\\] "
                + "((Guard #(\\d+) begins shift)|(falls asleep)|(wakes up))";
        List<Entry> entries = new Input(2018, 4).match(regexp)
                .map(Entry::new)
                .sorted(Comparator.comparing(e -> e.time))
                .collect(Collectors.toList());
        
        int guard = 0;
        Calendar lastTime = null;
        Map<Integer, int[]> minutes = new HashMap<>();
        for (Entry e : entries) {
            if (e.action == Action.SHIFT) {
                guard = e.guard;
            } else if (e.action == Action.FALL) {
                lastTime = e.time;
                if (!minutes.containsKey(guard)) {
                    minutes.put(guard, new int[60]);
                }
            } else {
                int[] mas = minutes.get(guard);
                IntStream.range(lastTime.get(Calendar.MINUTE), e.time.get(Calendar.MINUTE))
                        .forEach(i -> mas[i]++);
            }
        }
        guard = minutes.entrySet().stream()
                .max(Comparator.comparing(x -> Arrays.stream(x.getValue()).sum()))
                .get().getKey();

        int max = Utils.maxIndex(minutes.get(guard));
        
        System.err.printf("%d %d %d\n", guard, max, guard * max);

        max = 0;
        int maxMin = 0;
        for (Map.Entry<Integer, int[]> e : minutes.entrySet()) {
            int[] value = e.getValue();
            int maxIndex = Utils.maxIndex(value);
            if (value[maxIndex] > maxMin) {
                maxMin = value[maxIndex];
                max = maxIndex;
                guard = e.getKey();
            }
        }
        System.err.printf("%d %d %d\n", guard, max, guard * max);
    }

}
