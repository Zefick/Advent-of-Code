package adventofcode2018;

import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/6
 */
public class Day06 {

    public static void main(String[] args) {
        int coords[] = new Input(2018, 6)
                .match("(\\d+), (\\d+)")
                .flatMapToInt(m -> IntStream.range(1, 3)
                        .map(i -> Integer.parseInt(m.group(i))))
                .toArray();
        int n = coords.length / 2;
        int[] nearest = new int[n];
        Set<Integer> infinite = new HashSet<>();

        int safePoints = 0;
        for (int i=0; i<500; i++) {
            for (int j=0; j<500; j++) {
                int m = 0;
                int minD = 2000;
                boolean b = true;
                int dsum = 0;
                for (int k=0; k<n; k++) {
                    int d = Math.abs(coords[k*2] - i) + Math.abs(coords[k*2+1] - j);
                    dsum += d;
                    if (d == minD) {
                        b = false;
                    } else if (d < minD) {
                        minD = d;
                        m = k;
                        b = true;
                    }
                }
                if (b) {
                    if (i == 0 || i == 499 || j == 0 || j == 499) {
                        infinite.add(m);
                    }
                    nearest[m]++;
                }
                if (dsum < 10000) {
                    safePoints++;
                }
            }
        }

        int index = IntStream.range(0, n)
                .filter(i -> !infinite.contains(i))
                .mapToObj(i -> i)
                .max(Comparator.comparing(i -> nearest[i]))
                .get();
        System.err.println(nearest[index]);
        System.err.println(safePoints);
    }

}
