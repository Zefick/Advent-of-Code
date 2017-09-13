
package adventofcode2016;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day10 {

    static class Bot {
        int in1, in2;
        int out1, out2;
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

    static void setValue(Bot b, int v) {
        if (b.in1 == 0) b.in1 = v;
        else if (v > b.in1) b.in2 = v;
        else {
            b.in2 = b.in1;
            b.in1 = v;
        };
    }

    static int outputs[] = new int[32];

    public static void main(String[] args) {

        Pattern p1 = Pattern.compile("bot (\\d+) gives low to (\\w+) (\\d+) and high to (\\w+) (\\d+)");
        Pattern p2 = Pattern.compile("value (\\d+) goes to bot (\\d+)");

        new Input(2016, "input10.txt").strings().forEach(s -> {
            Matcher m = p1.matcher(s);
            if (m.find()) {
                int n = Integer.parseInt(m.group(1));
                Bot b = getBot(n);
                int out1 = Integer.parseInt(m.group(3));
                int out2 = Integer.parseInt(m.group(5));
                b.out1 = m.group(2).equals("bot") ? out1 : -out1-1;
                b.out2 = m.group(4).equals("bot") ? out2 : -out2-1;
            } else {
                m = p2.matcher(s);
                if (m.find()) {
                    int v = Integer.parseInt(m.group(1));
                    int n = Integer.parseInt(m.group(2));
                    setValue(getBot(n), v);
                }
            }
        });
        while (!bots.isEmpty()) {
            new HashMap<>(bots).forEach((n, b) -> {
                if (b.in1 > 0 && b.in2 > 0) {
                    if (b.in1 == 17 && b.in2 == 61) {
                        System.out.println(n);
                    }
                    if (b.out1 >= 0) {
                        setValue(getBot(b.out1), b.in1);
                    } else {
                        outputs[-b.out1-1] = b.in1;
                    }
                    if (b.out2 >= 0) {
                        setValue(getBot(b.out2), b.in2);
                    } else {
                        outputs[-b.out2-1] = b.in2;
                    }
                    bots.remove(n);
                }
            });
        }
        System.out.println(outputs[0] * outputs[1] * outputs[2]);
    }

}
