
package adventofcode2015;

import java.util.Arrays;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/6
 */
public class Day06 {

    public static void main(String[] args) {
        int[][] grid1 = new int[1000][1000];
        int[][] grid2 = new int[1000][1000];
        new Input(2015, 6)
                .match(".* (\\d+),(\\d+) through (\\d+),(\\d+)")
                .forEach(m -> {
            int x1 = Integer.parseInt(m.group(1));
            int y1 = Integer.parseInt(m.group(2));
            int x2 = Integer.parseInt(m.group(3));
            int y2 = Integer.parseInt(m.group(4));
            int operation = m.group(0).startsWith("turn on") ? 0 :
                    m.group(0).startsWith("turn off") ? 1 : 2;
            for (int i=x1; i<=x2; ++i) {
                for (int j=y1; j<=y2; ++j) {
                    if (operation == 0) {
                        grid1[i][j] = 1;
                        grid2[i][j] += 1;
                    } else if (operation == 1) {
                        grid1[i][j] = 0;
                        grid2[i][j] = Math.max(0, grid2[i][j] - 1);
                    } else if (operation == 2) {
                        grid1[i][j] = 1 - grid1[i][j];
                        grid2[i][j] += 2;
                    }
                }
            }
        });
        System.err.println(
            Arrays.stream(grid1).flatMapToInt(line -> Arrays.stream(line)).sum());
        System.err.println(
            Arrays.stream(grid2).flatMapToInt(line -> Arrays.stream(line)).sum());
    }
}
