package adventofcode2016;

import java.awt.Point;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

import adventofcode2016.PathFinder.PathFinder2D;
import utils.Input;

/**
 * https://adventofcode.com/2016/day/24
 */
public class Day24 {

    static int map[][] = new int[42][];

    private static int findPath(Point src, Point dest) {
        if (src.equals(dest)) {
            return 0;
        }
        PathFinder2D pf = new PathFinder2D();
        pf.setMovePredicate(p -> map[p.y][p.x] != '#');
        pf.setFinishCallback(() -> pf.stop());
        pf.run(src, dest);
        return pf.steps;
    }

    public static void main(String[] args) {
        List<String> data = new Input(2016, 24).strings();

        Point pts[] = new Point[8];
        int paths[][] = new int[8][8];

        int i=0;
        for (String s : data) {
            map[i] = s.chars().toArray();
            for (int j=0; j<map[i].length; ++j) {
                if (map[i][j] >= '0' && map[i][j] <= '7') {
                    pts[map[i][j]-'0'] = new Point(j, i);
                }
            }
            i++;
        }

        IntStream.range(0, 8).forEach(
                k -> IntStream.range(0, 8).forEach(
                j -> paths[k][j] = findPath(pts[k], pts[j])));

        List<Integer> steps = Arrays.asList(1, 2, 3, 4, 5, 6, 7);

        int min1 = Integer.MAX_VALUE;
        int min2 = min1;
        for (i=0; i<100000; i++) {
            Collections.shuffle(steps);
            int len1 = paths[0][steps.get(0)] +
                    IntStream.range(0, 6).map(x -> paths[steps.get(x)][steps.get(x+1)]).sum();
            int len2 = len1 + paths[steps.get(6)][0];
            if (len1 < min1) min1 = len1;
            if (len2 < min2) min2 = len2;
        }
        System.err.println(min1);
        System.err.println(min2);
    }

}
