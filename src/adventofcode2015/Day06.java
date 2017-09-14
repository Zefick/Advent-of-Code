
package adventofcode2015;

import java.util.Arrays;
import java.util.List;
import java.util.function.IntUnaryOperator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day06 {

    public static void main(String[] args) {
        Pattern p = Pattern.compile(".* (\\d+),(\\d+) through (\\d+),(\\d+)");

        List<String> input = new Input(2015, "input06.txt").strings();
        int[][] grid = new int[1000][1000];

        for (String command : input) {
            Matcher m = p.matcher(command);
            m.find();
            int x1 = Integer.parseInt(m.group(1));
            int y1 = Integer.parseInt(m.group(2));
            int x2 = Integer.parseInt(m.group(3));
            int y2 = Integer.parseInt(m.group(4));
            IntUnaryOperator proc;
            if (command.startsWith("turn on")) {
                proc = n -> n+1;
            } else if (command.startsWith("turn off")) {
                proc = n -> n>1 ? n-1 : 0;
            } else {
                proc = n -> n+2;
            }
            for (int i=x1; i<=x2; ++i) {
                for (int j=y1; j<=y2; ++j) {
                    grid[i][j] = proc.applyAsInt(grid[i][j]);
                }
            }
        }
        System.out.println(Arrays.stream(grid).mapToInt(
                line -> Arrays.stream(line).sum()).sum());
    }

}
