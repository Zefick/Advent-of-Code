
package adventofcode2017;

import java.util.List;

import utils.Input;

public class Day05 {

    public static void main(String[] args) throws Exception {
        List<String> input = new Input(2017, "input05.txt").strings();

        int[] commands = input.stream()
                .mapToInt(Integer::parseInt)
                .toArray();

        int steps = 0;
        for (int offset = 0;offset >= 0 && offset < commands.length;) {
            steps++;
            int tmp = offset;
            offset += commands[offset];
            commands[tmp]++;
        }
        System.out.println(steps);
    }

}
