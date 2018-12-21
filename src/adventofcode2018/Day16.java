package adventofcode2018;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/16
 */
public class Day16 {

    static BiFunction<int[], int[], int[]> makeFunc(BiFunction<int[], int[], Integer> op) {
        return (int[] instruction, int[] in) -> {
            int out[] = in.clone();
            out[instruction[3]] = op.apply(instruction, in);
            return out;
        };
    }

    public static void main(String[] args) {
        List<String> input = new Input(2018, 16).strings();
        Pattern p = Pattern.compile(".{9}(\\d+), (\\d+), (\\d+), (\\d+)");
        ArrayList<BiFunction<int[], int[], int[]>> opcodes = new ArrayList<>();
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] + in[instruction[2]]));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] + instruction[2]));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] * in[instruction[2]]));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] * instruction[2]));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] & in[instruction[2]]));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] & instruction[2]));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] | in[instruction[2]]));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] | instruction[2]));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]]));
        opcodes.add(makeFunc((instruction, in) -> instruction[1]));
        opcodes.add(makeFunc((instruction, in) -> instruction[1] > in[instruction[2]] ? 1 : 0));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] > instruction[2] ? 1 : 0));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] > in[instruction[2]] ? 1 : 0));
        opcodes.add(makeFunc((instruction, in) -> instruction[1] == in[instruction[2]] ? 1 : 0));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] == instruction[2] ? 1 : 0));
        opcodes.add(makeFunc((instruction, in) -> in[instruction[1]] == in[instruction[2]] ? 1 : 0));
        int part1 = 0;
        List<List<BiFunction<int[], int[], int[]>>> posibilities = IntStream.range(0, 16)
                .mapToObj(__ -> new ArrayList<>(opcodes))
                .collect(Collectors.toList());
        int n = 0;
        while (input.get(n).startsWith("Before")) {
            Matcher m1 = p.matcher(input.get(n));
            m1.find();
            int[] in = IntStream.range(1, 5).map(i -> Integer.parseInt(m1.group(i))).toArray();
            int[] instruction = Arrays.stream(input.get(n+1).split(" ")).mapToInt(Integer::parseInt).toArray();
            Matcher m2 = p.matcher(input.get(n+2));
            m2.find();
            int[] out = IntStream.range(1, 5).map(i -> Integer.parseInt(m2.group(i))).toArray();
            List<BiFunction<int[], int[], int[]>> possibleOpcodes = opcodes.stream()
                    .filter(op -> Arrays.equals(op.apply(instruction, in), out))
                    .collect(Collectors.toList());
            if (possibleOpcodes.size() >= 3) {
                part1++;
            }
            posibilities.get(instruction[0])
                    .removeIf(opcode -> !possibleOpcodes.contains(opcode));
            n += 4;
        }
        System.err.println(part1);
        for (int i=0; i<16; i++) {
            posibilities.stream()
                    .filter(ops -> ops.size() == 1)
                    .forEach(ops -> posibilities.stream()
                            .filter(ops2 -> ops2.size() > 1)
                            .forEach(ops2 -> ops2.remove(ops.get(0))));
        }
        int registers[] = {0, 0, 0, 0};
        for (n = n+2; n < input.size(); n++) {
            int[] instruction = Arrays.stream(input.get(n).split(" ")).mapToInt(Integer::parseInt).toArray();
            registers = posibilities.get(instruction[0]).get(0).apply(instruction, registers);
        }
        System.err.println(registers[0]);
    }
}
