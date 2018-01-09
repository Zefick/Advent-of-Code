package adventofcode2015;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day07 {

    static Map<String, Object> gates = new HashMap<>();

    enum Gate {
        NOT, AND, OR, LSHIFT, RSHIFT
    }

    static int resolve(Object g) {
        if (g instanceof Integer) {
            return (Integer) g;
        } else if (g instanceof String) {
            String name = (String)g;
            if (name.matches("\\d+")) {
                return Integer.parseInt(name);
            }
            int result = resolve(gates.get(name));
            gates.put(name, result);
            return result;
        } else if (g instanceof Object[]) {
            Object[] m = (Object[]) g;
            switch ((Gate) m[0]) {
            case NOT: return ~resolve(m[1]);
            case AND: return resolve(m[1]) & resolve(m[2]);
            case OR: return resolve(m[1]) | resolve(m[2]);
            case LSHIFT: return resolve(m[1]) << resolve(m[2]);
            case RSHIFT: return resolve(m[1]) >> resolve(m[2]);
            }
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        //                           2       3      4    5       67      8      9           10
        Pattern p = Pattern.compile("((\\d+)|(\\w+)|(NOT (\\w+))|((\\w+) (\\w+) (\\w+))) -> (\\w+)");
        List<String> input = new Input(2015, "input07.txt").strings();

        for (String str : input) {
            Matcher mt = p.matcher(str);
            mt.find();
            String name = mt.group(10);
            if (mt.group(2) != null) {
                gates.put(name, Integer.valueOf(mt.group(2)));
            } else if (mt.group(3) != null) {
                gates.put(name, mt.group(3));
            } else if (mt.group(4) != null) {
                gates.put(name, new Object[] { Gate.NOT, mt.group(5) });
            } else if (mt.group(6) != null) {
                String in1 = mt.group(7), in2 = mt.group(9);
                if (mt.group(8).equals("AND")) {
                    gates.put(name, new Object[] { Gate.AND, in1, in2 });
                } else if (mt.group(8).equals("OR")) {
                    gates.put(name, new Object[] { Gate.OR, in1, in2 });
                } else if (mt.group(8).equals("LSHIFT")) {
                    gates.put(name, new Object[] { Gate.LSHIFT, in1, in2 });
                } else if (mt.group(8).equals("RSHIFT")) {
                    gates.put(name, new Object[] { Gate.RSHIFT, in1, in2 });
                }
            }
        }
        gates.put("b", 46065);
        System.out.println(resolve(gates.get("a")));
    }
}
