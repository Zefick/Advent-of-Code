package adventofcode2018;

import java.awt.Point;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/17
 */
public class Day17 {

    public static void main(String[] args) {
        List<String> input = new Input(2018, 17).strings();
        Pattern p = Pattern.compile("(.)=(\\d+), .=(\\d+)..(\\d+)");
        Set<Point> clay = new HashSet<>();
        for (String s : input) {
            Matcher m = p.matcher(s);
            m.find();
            int x = Integer.parseInt(m.group(2));
            int a = Integer.parseInt(m.group(3));
            int b = Integer.parseInt(m.group(4));
            for (int y=a; y<=b; y++) {
                clay.add(m.group(1).equals("x")
                        ? new Point(x, y)
                        : new Point(y, x));
            }
        }
        int minx = clay.stream().mapToInt(pt -> pt.x).min().getAsInt();
        int maxx = clay.stream().mapToInt(pt -> pt.x).max().getAsInt();
        int miny = clay.stream().mapToInt(pt -> pt.y).min().getAsInt();
        int maxy = clay.stream().mapToInt(pt -> pt.y).max().getAsInt();
        System.out.printf("x[%d:%d], y[%d:%d]", minx, maxx, miny, maxy);

        Set<Point> flow = new HashSet<>();
        Set<Point> water = new HashSet<>();
        flow.add(new Point(500, miny));
        Set<Point> wet = new HashSet<>(flow);
        for (;!flow.isEmpty();) {
            Set<Point> nextFlow = new HashSet<>();
            for (Point drop : flow) {
                if (drop.y > maxy) continue;
                wet.add(drop);
                if (!clay.contains(new Point(drop.x, drop.y+1)) && !water.contains(new Point(drop.x, drop.y+1))) {
                    nextFlow.add(new Point(drop.x, drop.y+1));
                    continue;
                }
                Integer borderLeft = drop.x - 1;
                for (;;) {
                    Point left = new Point(borderLeft, drop.y);
                    if (clay.contains(left)) {
                        break;
                    }
                    if (clay.contains(new Point(borderLeft, drop.y + 1))
                            || water.contains(new Point(borderLeft, drop.y + 1))) {
                        wet.add(left);
                        borderLeft--;
                    } else {
                        nextFlow.add(left);
                        borderLeft = null;
                        break;
                    }
                }
                Integer borderRight = drop.x + 1;
                for (;;) {
                    Point right = new Point(borderRight, drop.y);
                    if (clay.contains(right)) {
                        break;
                    }
                    if (clay.contains(new Point(borderRight, drop.y + 1))
                            || water.contains(new Point(borderRight, drop.y + 1))) {
                        wet.add(right);
                        borderRight++;
                    } else {
                        nextFlow.add(right);
                        borderRight = null;
                        break;
                    }
                }
                if (borderLeft != null && borderRight != null) {
                    for (int x = borderLeft+1; x <= borderRight-1; x++) {
                        water.add(new Point(x, drop.y));
                    }
                    nextFlow.add(new Point(drop.x, drop.y-1));
                }
            }
            flow = nextFlow;
        }
        System.err.println(wet.size());
        System.err.println(water.size());
    }
}
