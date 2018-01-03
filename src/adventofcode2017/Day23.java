
package adventofcode2017;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import utils.Input;

public class Day23 {

    static long getVal(String id, Map<String, Long> registers) {
        return Character.isAlphabetic(id.charAt(0))
                ? registers.getOrDefault(id, 0l)
                : Integer.parseInt(id);
    }

    public static void main(String[] args) {
        List<String> input = new Input(2017, "input23.txt").strings();

        Map<String, Long> registers = new HashMap<>();
        int cnt = 0;
        int pointer = 0;

        for (;pointer >= 0 && pointer < input.size();) {
            String command = input.get(pointer);
            String parts[] = command.split(" ");
            switch (parts[0]) {
                case "set":
                    registers.put(parts[1], getVal(parts[2], registers));
                    break;
                case "sub":
                    registers.put(parts[1], registers.getOrDefault(parts[1], 0l) - getVal(parts[2], registers));
                    break;
                case "mul":
                    registers.put(parts[1], registers.getOrDefault(parts[1], 0l) * getVal(parts[2], registers));
                    cnt++;
                    break;
                case "jnz":
                    if (getVal(parts[1], registers) != 0) {
                        pointer += getVal(parts[2], registers);
                        continue;
                    }
                    break;
            }
            pointer++;
        }
        System.out.println(cnt);
    }
}
