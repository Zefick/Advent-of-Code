
package adventofcode2017;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day08 {

    public static void main(String[] args) throws Exception {
        List<String> input = new Input(2017, "input08.txt").strings();
        //                           1      2         3            4      5          6
        Pattern p = Pattern.compile("(\\w+) (inc|dec) (-?\\d+) if (\\w+) ([><=!]{1,2}) (-?\\d+)");

        Map<String, Integer> registers = new HashMap<>();
        int max = 0, localMax = 0;
        for (String s : input) {
            Matcher m = p.matcher(s);
            m.find();
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
            localMax = registers.values().stream().max(Integer::compareTo).get();
            max = Math.max(max, localMax);
        }
        System.out.println(localMax);
        System.out.println(max);
    }
}
