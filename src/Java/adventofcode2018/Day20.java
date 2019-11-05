package adventofcode2018;

import java.awt.Point;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/20
 */
public class Day20 {

    static int route(Point pt, String path, int steps, Map<Point, Integer> map) {
        int mySteps = 0;
        Point myPoint = pt;
        for (int i=0; ; i++) {
            Point next = null;
            char c = path.charAt(i);
            if (c == 'E') {
                next = new Point(myPoint.x + 1, myPoint.y);
            } else if (c == 'W') {
                next = new Point(myPoint.x - 1, myPoint.y);
            } else if (c == 'N') {
                next = new Point(myPoint.x, myPoint.y - 1);
            } else if (c == 'S') {
                next = new Point(myPoint.x, myPoint.y + 1);
            } else if (c == '(') {
                i += route(myPoint, path.substring(i+1), steps + mySteps, map);
                continue;
            } else if (c == ')' || c =='$') {
                return i + 1;
            } else if (c == '|') {
                myPoint = pt;
                mySteps = 0;
            }
            if (next != null) {
                myPoint = next;
                mySteps++;
                if (!map.containsKey(next)) {
                    map.put(next, steps + mySteps);
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        String input = new Input(2018, 20).strings().get(0);
        Map<Point, Integer> map = new HashMap<>();
        route(new Point(0, 0), input, 0, map);

        System.err.println(map.values().stream().max(Comparator.naturalOrder()).get());
        System.err.println(map.values().stream().filter(x -> x >= 1000).count());
        System.err.println();
    }
}
