package adventofcode2018;

import java.util.Arrays;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/10
 */
public class Day10 {
    
    public static void main(String[] args) {
        int[][] data = new Input(2018, 10)
                .match("position=<\\s*(.+),\\s*(.+)> velocity=<\\s*(.+),\\s*(.+)>")
                .map(m -> IntStream.range(1, 5)
                        .map(i -> Integer.parseInt(m.group(i)))
                        .toArray())
                .toArray(int[][]::new);

        for (int n=0; n<50000; n++) {
            int x1 = 1000000, x2 = -1000000, y1 = 1000000, y2 = -1000000;
            for (int[] star : data) {
                if (star[0] < x1) x1 = star[0];
                if (star[0] > x2) x2 = star[0];
                if (star[1] < y1) y1 = star[1];
                if (star[1] > y2) y2 = star[1];
            }
            if (y2-y1 < 15) {
                for (int i = -2; i < y2-y1+3; i++) {
                    for (int j = -2; j < x2-x1+3; j++) {
                        int x = x1+j, y = y1+i;
                        boolean b = Arrays.stream(data).anyMatch(d -> d[0]==x && d[1]==y);
                        System.out.print(b ? '#' : ' ');
                    }
                    System.out.println();
                }
                System.err.println(n);
            }
            for (int[] star : data) {
                star[0] += star[2];
                star[1] += star[3];
            }
        }
    }

}
