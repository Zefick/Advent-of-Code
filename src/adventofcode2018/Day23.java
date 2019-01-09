package adventofcode2018;

import java.util.*;
import java.util.stream.*;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/23
 */
public class Day23 {

    static class Region implements Comparable<Region> {
        final int x, y, z, r;
        int bots;
        Region(int x, int y, int z, int r) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.r = r;
        }
        boolean testContains(int[] bot) {
            return bot[3] >=
                    Math.max(x - bot[0], 0) + Math.max(bot[0] - x - r, 0)
                  + Math.max(y - bot[1], 0) + Math.max(bot[1] - y - r, 0)
                  + Math.max(z - bot[2], 0) + Math.max(bot[2] - z - r, 0);
        }
        @Override
        public int compareTo(Region reg) {
            if (bots != reg.bots) return bots - reg.bots;
            if (r != reg.r) return reg.r - r;
            if (x + y + z > reg.x + reg.y + reg.z) return 1;
            if (x + y + z < reg.x + reg.y + reg.z) return -1;
            return hashCode();
        }
    }

    public static void main(String[] args) throws Exception {
        List<int[]> bots = new Input(2018, 23)
                .match("pos=<(.+),(.+),(.+)>, r=(.+)")
                .map(m -> IntStream.range(1, 5)
                        .map(i -> Integer.parseInt(m.group(i)))
                        .toArray())
                .collect(Collectors.toList());

        int[] max = bots.stream().max(Comparator.comparing(b -> b[3])).get();
        System.err.println(bots.stream()
                .filter(b -> Math.abs(b[0]-max[0]) + Math.abs(b[1]-max[1]) + Math.abs(b[2]-max[2]) <= max[3])
                .count());

        int xMin = bots.stream().mapToInt(b -> b[0]).min().getAsInt();
        int xMax = bots.stream().mapToInt(b -> b[0]).max().getAsInt();
        int yMin = bots.stream().mapToInt(b -> b[1]).min().getAsInt();
        int yMax = bots.stream().mapToInt(b -> b[1]).max().getAsInt();
        int zMin = bots.stream().mapToInt(b -> b[2]).min().getAsInt();
        int zMax = bots.stream().mapToInt(b -> b[2]).max().getAsInt();
        int rMax = Math.max(Math.max(xMax - xMin, yMax - yMin), zMax - zMin);
        int R = 1;
        while (R < rMax) R *= 2;

        Region region = new Region(
                (xMax + xMin - R) / 2, (yMax + yMin - R) / 2,
                (zMax + zMin - R) / 2, R);
        region.bots = (int)bots.stream().filter(region::testContains).count();
        TreeSet<Region> map = new TreeSet<>(Collections.singleton(region));
        for (int boxes = 1; ; boxes++) {
            Region reg = map.pollLast();
            if (reg.r == 0) {
                System.err.println(reg.x + reg.y + reg.z);
                System.out.printf("%d bots, %d boxes scanned", reg.bots, boxes);
                break;
            }
            int r = reg.r / 2;
            for (int i=0; i<8; i++) {
                Region child = new Region(reg.x + r*(i&1), reg.y + r*(i/2&1), reg.z + r*(i/4&1), r);
                child.bots = (int)bots.stream().filter(child::testContains).count();
                map.add(child);
            }
        }
    }
}
