package adventofcode2016;

import java.awt.Point;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Day13 {

    static boolean isEmpty(int x, int y) {
        return x >= 0 && y >= 0 &&
            Integer.toBinaryString((x+3)*x + (2*x + y + 1)*y + 1352)
                    .chars()
                    .filter(c -> c=='1')
                    .count() % 2 == 0;
    }

    public static void main(String[] args) {

        Point dest = new Point(31, 39);

        Set<Point> visited = new HashSet<>();
        List<Point> current = new ArrayList<>();
        current.add(new Point(1, 1));
        int len = 0;
        int dirs[][] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!current.isEmpty()) {
            len++;
            current = current.stream()
                .flatMap(p -> Stream.of(dirs).map(d -> new Point(p.x+d[1], p.y+d[0])))
                .distinct()
                .filter(p -> !visited.contains(p) && isEmpty(p.x, p.y))
                .collect(Collectors.toList());
            if (current.contains(dest)) {
                break;
            }
            visited.addAll(current);
            if (len == 50) {
                System.out.println("visited cells: " + visited.size());
            }
        }
        System.out.println("path length: " + len);
    }

}
