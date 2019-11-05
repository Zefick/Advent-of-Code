
package adventofcode2017;

import java.util.HashMap;
import java.util.Map;

import utils.Input;

/**
 * https://adventofcode.com/2017/day/8
 */
public class Day08 {

    public static void main(String[] args) throws Exception {
        Map<String, Integer> registers = new HashMap<>();
        int max[] = {0, 0};
        new Input(2017, 8)
                .match("(\\w+) (inc|dec) (-?\\d+) if (\\w+) ([><=!]{1,2}) (-?\\d+)")
                .forEach(m -> {
            int b = Integer.parseInt(m.group(6));
            int regnum = registers.getOrDefault(m.group(4), 0);
            boolean cond = false;
            switch (m.group(5)) {
                case "==" : cond = regnum == b; break;
                case "!=" : cond = regnum != b; break;
                case ">" :  cond = regnum >  b; break;
                case "<" :  cond = regnum <  b; break;
                case ">=" : cond = regnum >= b; break;
                case "<=" : cond = regnum <= b; break;
            }
            if (cond) {
                int a = Integer.parseInt(m.group(3));
                regnum = registers.getOrDefault(m.group(1), 0)
                        + ((m.group(2).equals("inc")) ? +a : -a);
                registers.put(m.group(1), regnum);
            }
            max[1] = registers.values().stream().max(Integer::compareTo).get();
            max[0] = Math.max(max[0], max[1]);
        });
        System.out.println(max[1]);
        System.out.println(max[0]);
    }
}
