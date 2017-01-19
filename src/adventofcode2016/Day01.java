
package adventofcode2016;

import java.awt.Point;
import java.util.HashSet;
import java.util.Set;

public class Day01 {

    static String data = "R3, R1, R4, L4, R3, R1, R1, L3, L5, L5, L3, R1, R4, L2, L1, R3, L3, R2, R1, R1, L5, L2, L1, "
            + "R2, L4, R1, L2, L4, R2, R2, L2, L4, L3, R1, R4, R3, L1, R1, L5, R4, L2, R185, L2, R4, R49, L3, L4, R5, "
            + "R1, R1, L1, L1, R2, L1, L4, R4, R5, R4, L3, L5, R1, R71, L1, R1, R186, L5, L2, R5, R4, R1, L5, L2, R3, "
            + "R2, R5, R5, R4, R1, R4, R2, L1, R4, L1, L4, L5, L4, R4, R5, R1, L2, L4, L1, L5, L3, L5, R2, L5, R4, "
            + "L4, R3, R3, R1, R4, L1, L2, R2, L1, R4, R2, R2, R5, R2, R5, L1, R1, L4, R5, R4, R2, R4, L5, R3, R2, "
            + "R5, R3, L3, L5, L4, L3, L2, L2, R3, R2, L1, L1, L5, R1, L3, R3, R4, R5, L3, L5, R1, L3, L5, L5, L2, "
            + "R1, L3, L1, L3, R4, L1, R3, L2, L2, R3, R3, R4, R4, R1, L4, R1, L5";

    public static void main(String[] args) {
        int dx = 0, dy = 1;
        Point coord = new Point(0, 0);
        String steps[] = data.split(", ");
        Set<Point> track = new HashSet<>();
        track.add(coord);

        loop:
        for (String s : steps) {
            boolean isRight = s.charAt(0) == 'R';
            int tmp = dx;
            dx = isRight ? dy : -dy;
            dy = isRight ? -tmp : tmp;
            int len = Integer.parseInt(s.substring(1));
            for (int i=0; i<len; ++i) {
                coord = coord.getLocation();
                coord.translate(dx, dy);
                if (track.contains(coord)) {
                    break loop;
                }
                track.add(coord);
            }
        }
        System.out.println(Math.abs(coord.x) + Math.abs(coord.y));
    }

}
