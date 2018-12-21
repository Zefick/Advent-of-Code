package adventofcode2018;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.BiFunction;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/19
 */
public class Day19 {

    static BiFunction<int[], int[], int[]> makeFunc(BiFunction<int[], int[], Integer> op) {
        return (int[] instruction, int[] in) -> {
            int out[] = in.clone();
            out[instruction[3]] = op.apply(instruction, in);
            return out;
        };
    }

    public static void main(String[] args) throws Exception {
        List<String> program = new Input(2018, 19).strings();
        int ip = 3;
        program.remove(0);
        Map<String, BiFunction<int[], int[], int[]>> opcodes = new HashMap<>();
        opcodes.put("addr", makeFunc((instruction, in) -> in[instruction[1]] + in[instruction[2]]));
        opcodes.put("addi", makeFunc((instruction, in) -> in[instruction[1]] + instruction[2]));
        opcodes.put("mulr", makeFunc((instruction, in) -> in[instruction[1]] * in[instruction[2]]));
        opcodes.put("muli", makeFunc((instruction, in) -> in[instruction[1]] * instruction[2]));
        opcodes.put("banr", makeFunc((instruction, in) -> in[instruction[1]] & in[instruction[2]]));
        opcodes.put("bani", makeFunc((instruction, in) -> in[instruction[1]] & instruction[2]));
        opcodes.put("borr", makeFunc((instruction, in) -> in[instruction[1]] | in[instruction[2]]));
        opcodes.put("bori", makeFunc((instruction, in) -> in[instruction[1]] | instruction[2]));
        opcodes.put("setr", makeFunc((instruction, in) -> in[instruction[1]]));
        opcodes.put("seti", makeFunc((instruction, in) -> instruction[1]));
        opcodes.put("gtir", makeFunc((instruction, in) -> instruction[1] > in[instruction[2]] ? 1 : 0));
        opcodes.put("gtri", makeFunc((instruction, in) -> in[instruction[1]] > instruction[2] ? 1 : 0));
        opcodes.put("gtrr", makeFunc((instruction, in) -> in[instruction[1]] > in[instruction[2]] ? 1 : 0));
        opcodes.put("eqir", makeFunc((instruction, in) -> instruction[1] == in[instruction[2]] ? 1 : 0));
        opcodes.put("eqri", makeFunc((instruction, in) -> in[instruction[1]] == instruction[2] ? 1 : 0));
        opcodes.put("eqrr", makeFunc((instruction, in) -> in[instruction[1]] == in[instruction[2]] ? 1 : 0));
        Pattern p = Pattern.compile("(\\w+) (\\d+) (\\d+) (\\d+)");
        for (int v = 0; v<=1; v++) {
            int regs[] = {v, 0, 0, 0, 0, 0};
            for (int t = 0; t < 1000; t++) {
                int ptr = regs[ip];
                if (ptr < 0 || ptr > program.size()-1) {
                    break;
                }
                String command = program.get(ptr);
                Matcher m = p.matcher(command);
                m.find();
                String opcode = m.group(1);
                int instruction[] = new int[4];
                instruction[1] = Integer.parseInt(m.group(2));
                instruction[2] = Integer.parseInt(m.group(3));
                instruction[3] = Integer.parseInt(m.group(4));
                regs = opcodes.get(opcode).apply(instruction, regs);
                regs[ip]++;
            }
            System.err.println(regs[5] + regs[5] / 2 + 3);
        }
    }
}
