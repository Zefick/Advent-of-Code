package adventofcode2018;

import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/10
 */
public class Day10 {

    static Pattern p = Pattern.compile("position=<\\s*(-?\\d+),\\s*(-?\\d+)> velocity=<\\s*(-?\\d+),\\s*(-?\\d+)>");
    
    public static void main(String[] args) {
        List<String> input = new Input(2018, "input10.txt").strings();
        int[][] data = input.stream().map(s -> {
            Matcher m = p.matcher(s);
            m.find();
            return IntStream.range(1, 5)
                    .map(i -> Integer.parseInt(m.group(i)))
                    .toArray();
        }).toArray(int[][]::new);

        for (int n=0; n<50000; n++) {
            int x1 = 1000000, x2 = -1000000, y1 = 1000000, y2 = -1000000;
            for (int[] star : data) {
                if (star[0] < x1) x1 = star[0];
                if (star[0] > x2) x2 = star[0];
                if (star[1] < y1) y1 = star[1];
                if (star[1] > y2) y2 = star[1];
            }
            if (y2-y1 < 15) {
                System.out.printf("[%d %d %d %d %d]\n", x1, x2, y1, y2, n);
                for (int i = -2; i < y2-y1+3; i++) {
                    for (int j = -2; j < x2-x1+3; j++) {
                        int x = x1+j, y = y1+i;
                        boolean b = Arrays.stream(data).anyMatch(d -> d[0]==x && d[1]==y);
                        System.out.print(b ? '#' : '.');
                    }
                    System.out.println();
                }
                System.out.println();
            }
            for (int[] star : data) {
                star[0] += star[2];
                star[1] += star[3];
            }
        }
    }

}