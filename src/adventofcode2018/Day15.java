package adventofcode2018;

import java.awt.Point;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/15
 */
public class Day15 {

    static class Unit {
        int x, y;
        int hp = 200;
        int type;
        Unit(int x, int y, int type) {
            this.x = x;
            this.y = y;
            this.type = type;
        }
    }

    static int opposite(int type) {
        return type == 'E' ? 'G' : 'E';
    }

    static final int[][] dirs = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};

    static Point wave(int[][] map, Predicate<Point> pred, Point start) {
        List<Point> points = Collections.singletonList(start);
        Set<Point> visited = new HashSet<>();
        Point target = null;
        // find nearest point that satisfies the condition
        while (!points.isEmpty() && target == null) {
            List<Point> nextPoints = new ArrayList<>();
            for (Point p : points) {
                for (int dir[] : dirs) {
                    Point p2 = new Point(p.x+dir[0], p.y+dir[1]);
                    if (visited.contains(p2)) {
                        continue;
                    }
                    if (pred.test(p2)) {
                        if (target == null || p.y < target.y || (p.y == target.y && p.x < target.x)) {
                            target = p;
                        }
                    }
                    if (map[p2.y][p2.x] == '.') {
                        nextPoints.add(p2);
                        visited.add(p2);
                    }
                }
            }
            points = nextPoints;
        }
        return target;
    }

    public static void main(String[] args) {
        long time = System.currentTimeMillis();
        List<String> results = new ArrayList<>();
        for (int power = 3; ; power++) {
            int t = 0;
            int powerFinal = power;
            int[][] map = new Input(2018, 15).getMap();
            List<Unit> units = new ArrayList<>();
            // collect all the units
            for (int y=0; y<map.length; y++) {
                for (int x=0; x<map[y].length; x++) {
                    if (map[y][x] == 'E' || map[y][x] == 'G') {
                        units.add(new Unit(x, y, map[y][x]));
                    }
                }
            }
            for (;/* rounds */;) {
                boolean end = true;
                units.sort(Comparator.comparing(u -> u.y*1000 + u.x));
                for (Unit u : units) {
                    if (u.hp <= 0) continue;
                    // find nearest target
                    Point target = wave(map,
                            p -> map[p.y][p.x] == opposite(u.type),
                            new Point(u.x, u.y));
                    if (target == null) {
                        continue;
                    }
                    end = false;
                    // move if needed
                    if (target.x != u.x || target.y != u.y) {
                        target = wave(map, p -> p.x == u.x && p.y == u.y, target);
                        map[u.y][u.x] = '.';
                        map[target.y][target.x] = u.type;
                        u.x = target.x;
                        u.y = target.y;
                    }
                    // atack if possible
                    Arrays.stream(dirs)
                            .filter(dir -> map[u.y+dir[1]][u.x+dir[0]] == opposite(u.type))
                            .map(dir -> units.stream()
                                    .filter(u2 -> u2.x == u.x+dir[0] && u2.y == u.y+dir[1] && u2.hp > 0)
                                    .findFirst().get())
                            .sorted(Comparator.comparing(u2 -> u2.hp * 10000 + u2.y * 100 + u2.x))
                            .findFirst().ifPresent(u2 -> {
                                u2.hp -= u.type == 'E' ? powerFinal : 3;
                                if (u2.hp <= 0) map[u2.y][u2.x] = '.';
                            });
                }
                if (end) {
                    break;
                }
                t++;
            }
            int sumHP = units.stream().mapToInt(u -> u.hp).filter(u -> u > 0).sum();
            results.add(String.format("power = %2d: %d * %d = %d", power, t-1, sumHP, (t-1) * sumHP));
            if (units.stream().noneMatch(u -> u.type == 'E' && u.hp <= 0)) {
                break;
            }
        }
        System.err.println(results.get(0));
        System.err.println(results.get(results.size() - 1));
        System.out.println("time: " + (System.currentTimeMillis() - time));
    }

    static void printMap(int[][] map) {
        Arrays.stream(map)
                .map(s -> Arrays.stream(s).mapToObj(c -> Character.toString((char)c))
                        .collect(Collectors.joining()))
                .forEach(System.out::println);
        System.out.println();
    }
}
