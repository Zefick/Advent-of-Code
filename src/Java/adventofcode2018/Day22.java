package adventofcode2018;

import java.awt.Point;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

/**
 * https://adventofcode.com/2018/day/22
 */
public class Day22 {

    static int depth = 9171;
    static int tx = 7, ty = 721;

    // erosion levels map
    static Map<Point, Integer> map = new HashMap<>();

    static int getLevel(Point p) {
        if (map.containsKey(p)) {
            return map.get(p);
        }
        int level;
        if (p.x == 0) {
            level = p.y * 48271;
        } else if (p.y == 0) {
            level = p.x * 16807;
        } else {
            level = getLevel(new Point(p.x, p.y-1)) * getLevel(new Point(p.x-1, p.y));
        }
        level = (level + depth) %  20183;
        map.put(p, level);
        return level;
    }

    static Map<Point, Integer> distances0 = new HashMap<>();
    static Map<Point, Integer> distances1 = new HashMap<>();
    static Map<Point, Integer> distances2 = new HashMap<>();
    static int getDistance(Point p, int tool) {
        if (tool == 0) return distances0.getOrDefault(p, Integer.MAX_VALUE);
        else if (tool == 1) return distances1.getOrDefault(p, Integer.MAX_VALUE);
        else return distances2.getOrDefault(p, Integer.MAX_VALUE);
    }
    static void putDistance(Point p, int tool, int d) {
        if (tool == 0) distances0.put(p, d);
        else if (tool == 1) distances1.put(p, d);
        else if (tool == 2) distances2.put(p, d);
    }

    public static void main(String[] args) throws Exception {
        // depth = 510;
        // tx = 10;
        // ty = 10;

        int risk = 0;
        for (int i=0; i<=ty; i++) {
            for (int j=0; j<=tx; j++) {
                risk += getLevel(new Point(j, i)) % 3;
            }
        }
        System.err.println(risk);

        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {0, 0, 1, 0});  // x, y, tool, time
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int k = 0; k<5_000_000; k++) {
            if (queue.isEmpty()) {
                System.out.println("finished after " + k + " steps");
                break;
            }
            int[] pos = queue.poll();
            Point p = new Point(pos[0], pos[1]);
            int tool = pos[2];
            int time = pos[3];
            if (p.x == tx && p.y == ty) {
                if (tool != 1) time += 7;
                putDistance(p, 1, Math.min(time, getDistance(p, 1)));
                continue;
            }
            if (getDistance(p, tool) < time || getDistance(new Point(tx, ty), 1) <= time)
                continue;
            int tool2 = 3 - (tool + getLevel(p) % 3);
            if (getDistance(p, tool2) > time + 7) {
                putDistance(p, tool2, time + 7);
                queue.add(new int[] {p.x, p.y, tool2, time + 7});
            }
            for (int dir[] : dirs) {
                Point p2 = new Point(p.x + dir[0], p.y + dir[1]);
                if (p2.x < 0 || p2.y < 0 || p2.x > 100 || getLevel(p2) % 3 == tool) {
                    continue;
                }
                if (getDistance(p2, tool) > time + 1) {
                    putDistance(p2, tool, time + 1);
                    queue.add(new int[] {p2.x, p2.y, tool, time + 1});
                }
            }
        }
        System.err.println(getDistance(new Point(tx, ty), 1));
    }
}
