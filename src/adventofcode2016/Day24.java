package adventofcode2016;

import java.awt.Point;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day24 {

    static int map[][] = new int[42][];

    private static int findPath(Point src, Point dest) {
        if (src.equals(dest)) {
            return 0;
        }
        Set<Point> visited = new HashSet<>();
        List<Point> current = new ArrayList<>();
        current.add(src);
        int len = 0;
        int dirs[][] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!current.isEmpty()) {
            len++;
            current = current.stream()
                .flatMap(p -> Stream.of(dirs).map(d -> new Point(p.x+d[1], p.y+d[0])))
                .distinct()
                .filter(p -> !visited.contains(p) && map[p.y][p.x] != '#')
                .collect(Collectors.toList());
            if (current.contains(dest)) {
                return len;
            }
            visited.addAll(current);
        }
        return len;
    }

    public static void main(String[] args) {
        List<String> data = Utils.getStringsFromFile("input24.txt");

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

        int min = Integer.MAX_VALUE;

        for (i=0; i<10000; i++) {
            Collections.shuffle(steps);
            int len = paths[0][steps.get(0)] + paths[steps.get(6)][0] +
                    IntStream.range(0, 6).map(x -> paths[steps.get(x)][steps.get(x+1)]).sum();
            if (len < min) {
                min = len;
            }
        }
        System.out.println(min);
    }

}
