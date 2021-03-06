
package adventofcode2015;

import java.util.HashSet;
import java.util.Set;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/3
 */
public class Day03 {

    private static int hash(int[] position) {
        return (position[0] * 10000 + position[1]) * 265443576 ;
    }

    public static void main(String[] args) {
        String input = new Input(2015, 3).strings().get(0);

        for (int k=1; k<=2; k++) {
            Set<Integer> visited = new HashSet<>();

            int positions[][] = {
                {0, 0},  // santa
                {0, 0}   // robo-santa
            };
            visited.add(hash(positions[0]));
            int n = 0;
            for (byte b : input.getBytes()) {
                int[] position = positions[n % k];
                n++;
                if (b == '<') position[0] -= 1;
                else if (b == '>') position[0] += 1;
                else if (b == 'v') position[1] -= 1;
                else if (b == '^') position[1] += 1;
                visited.add(hash(position));
            }
            System.err.println(visited.size());
        }
    }

}
