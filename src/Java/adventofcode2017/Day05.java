
package adventofcode2017;

import utils.Input;

/**
 * https://adventofcode.com/2017/day/5
 */
public class Day05 {

    public static void main(String[] args) throws Exception {
        int[] commands = new Input(2017, 5).strings().stream()
                .mapToInt(Integer::parseInt)
                .toArray();

        int steps = 0;
        int[] commands1 = commands.clone();
        for (int offset = 0;offset >= 0 && offset < commands1.length;) {
            steps++;
            int tmp = offset;
            offset += commands1[offset];
            commands1[tmp]++;
        }
        System.out.println(steps);
        
        steps = 0;
        int[] commands2 = commands.clone();
        for (int offset = 0;offset >= 0 && offset < commands2.length;) {
            steps++;
            int tmp = offset;
            offset += commands2[offset];
            if (commands2[tmp] >= 3) commands2[tmp]--;
            else commands2[tmp]++;
        }
        System.out.println(steps);
    }

}
