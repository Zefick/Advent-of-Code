
package adventofcode2016;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2016/day/10
 */
public class Day10 {

    static class Output {
        int value;
        void setValue(int v) {
            value = v;
        }
    }

    static class Bot extends Output {
        int in1, in2;
        Output out1, out2;
        void setValue(int v) {
            if (in1 == 0) in1 = v;
            else if (v > in1) in2 = v;
            else {
                in2 = in1;
                in1 = v;
            };
        }
    }

    static Map<Integer, Bot> bots = new HashMap<>();

    static Bot getBot(int n) {
        if (bots.containsKey(n)) {
            return bots.get(n);
        } else {
            Bot b = new Bot();
            bots.put(n, b);
            return b;
        }
    }

    static Output outputs[] = IntStream.range(0, 32).mapToObj(i -> new Output()).toArray(Output[]::new);

    public static void main(String[] args) {

        Pattern p1 = Pattern.compile("bot (\\d+) gives low to (\\w+) (\\d+) and high to (\\w+) (\\d+)");
        Pattern p2 = Pattern.compile("value (\\d+) goes to bot (\\d+)");

        new Input(2016, 10).strings().forEach(s -> {
            Matcher m = p1.matcher(s);
            if (m.find()) {
                int n = Integer.parseInt(m.group(1));
                Bot b = getBot(n);
                int out1 = Integer.parseInt(m.group(3));
                int out2 = Integer.parseInt(m.group(5));
                b.out1 = m.group(2).equals("bot") ? getBot(out1) : outputs[out1];
                b.out2 = m.group(4).equals("bot") ? getBot(out2) : outputs[out2];
            } else {
                m = p2.matcher(s);
                if (m.find()) {
                    int v = Integer.parseInt(m.group(1));
                    int n = Integer.parseInt(m.group(2));
                    getBot(n).setValue(v);
                }
            }
        });
        while (!bots.isEmpty()) {
            new HashMap<>(bots).forEach((n, b) -> {
                if (b.in1 > 0 && b.in2 > 0) {
                    if (b.in1 == 17 && b.in2 == 61) {
                        System.err.println(n);
                    }
                    b.out1.setValue(b.in1);
                    b.out2.setValue(b.in2);
                    bots.remove(n);
                }
            });
        }
        System.err.println(outputs[0].value * outputs[1].value * outputs[2].value);
    }

}
