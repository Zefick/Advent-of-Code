
package adventofcode2017;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import utils.Input;

public class Day18 {

    static long getVal(String id, Map<String, Long> registers) {
        return Character.isAlphabetic(id.charAt(0))
                ? registers.getOrDefault(id, 0l)
                : Integer.parseInt(id);
    }

    static class State {
        Map<String, Long> registers = new HashMap<>();
        int sent;
        int pointer;
        Deque<Long> queue = new ArrayDeque<>();
        boolean terminated = false;
        boolean waiting = false;
    }

    public static void main(String[] args) {
        List<String> input = new Input(2017, "input18.txt").strings();

        State states[] = {new State(), new State()};
        states[1].registers.put("p", 1l);
        int stateIndex = 1;
        State currentState = states[stateIndex];

        boolean part1 = false;

        loop:
        for (;;) {
            if (currentState.pointer < 0 || currentState.pointer >= input.size()) {
                currentState.terminated = true;
                stateIndex = (stateIndex + 1) & 1;
                currentState = states[stateIndex];
                if (currentState.terminated) {
                    stateIndex = 0;
                    break;
                }
            }

            String command = input.get(currentState.pointer);
            String parts[] = command.split(" ");
            Map<String, Long> registers = currentState.registers;
            switch (parts[0]) {
                case "snd":
                    states[(stateIndex + 1) & 1].queue.add(getVal(parts[1], registers));
                    currentState.sent++;
                    break;
                case "set":
                    registers.put(parts[1], getVal(parts[2], registers));
                    break;
                case "add":
                    registers.put(parts[1], registers.getOrDefault(parts[1], 0l) + getVal(parts[2], registers));
                    break;
                case "mul":
                    registers.put(parts[1], registers.getOrDefault(parts[1], 0l) * getVal(parts[2], registers));
                    break;
                case "mod":
                    registers.put(parts[1], registers.getOrDefault(parts[1], 0l) % getVal(parts[2], registers));
                    break;
                case "rcv":
                    if (!currentState.queue.isEmpty()) {
                        if (!part1) {
                            part1 = true;
                            System.out.println(currentState.queue.peekLast());
                        }
                        registers.put(parts[1], currentState.queue.poll());
                    } else {
                        currentState.waiting = true;
                        stateIndex = (stateIndex + 1) & 1;
                        currentState = states[stateIndex];
                        if ((currentState.waiting && currentState.queue.isEmpty()) || currentState.terminated) {
                            stateIndex = 0;
                            break loop;
                        }
                        continue loop;
                    }
                    break;
                case "jgz":
                    if (getVal(parts[1], registers) > 0) {
                        currentState.pointer += getVal(parts[2], registers);
                        continue loop;
                    }
                    break;
            }
            currentState.pointer++;
        }
        System.out.println(states[1].sent);
    }
}
