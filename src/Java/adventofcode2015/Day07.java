package adventofcode2015;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/7
 */
public class Day07 {

    enum Gate {
        NOT, AND, OR, LSHIFT, RSHIFT
    }

    static int resolve(Object g, Map<String, Object> gates) {
        if (g instanceof Integer) {
            return (Integer) g;
        } else if (g instanceof String) {
            String name = (String)g;
            if (name.matches("\\d+")) {
                return Integer.parseInt(name);
            }
            int result = resolve(gates.get(name), gates);
            gates.put(name, result);
            return result;
        } else if (g instanceof Object[]) {
            Object[] m = (Object[]) g;
            switch ((Gate) m[0]) {
            case NOT: return ~resolve(m[1], gates);
            case AND: return resolve(m[1], gates) & resolve(m[2], gates);
            case OR: return resolve(m[1], gates) | resolve(m[2], gates);
            case LSHIFT: return resolve(m[1], gates) << resolve(m[2], gates);
            case RSHIFT: return resolve(m[1], gates) >> resolve(m[2], gates);
            }
        }
        throw new IllegalArgumentException();
    }

    public static void main(String[] args) throws IOException {
        Map<String, Object> gates = new HashMap<>();
        new Input(2015, 7)
                 //      2             3          4      5      6           7
                .match("((\\w+)|(?:NOT (\\w+))|(?:(\\w+) (\\w+) (\\w+))) -> (\\w+)")
                .forEach(m -> {
            String name = m.group(7);
            if (m.group(2) != null) {
                gates.put(name, m.group(2));
            } else if (m.group(3) != null) {
                gates.put(name, new Object[] { Gate.NOT, m.group(3) });
            } else if (m.group(4) != null) {
                String in1 = m.group(4), in2 = m.group(6);
                if (m.group(5).equals("AND")) {
                    gates.put(name, new Object[] { Gate.AND, in1, in2 });
                } else if (m.group(5).equals("OR")) {
                    gates.put(name, new Object[] { Gate.OR, in1, in2 });
                } else if (m.group(5).equals("LSHIFT")) {
                    gates.put(name, new Object[] { Gate.LSHIFT, in1, in2 });
                } else if (m.group(5).equals("RSHIFT")) {
                    gates.put(name, new Object[] { Gate.RSHIFT, in1, in2 });
                }
            }
        });
        Map<String, Object> gates2 = new HashMap<>(gates);
        int a = resolve(gates.get("a"), gates);
        System.err.println(a);
        gates2.put("b", a);
        System.err.println(resolve(gates2.get("a"), gates2));
    }
}
