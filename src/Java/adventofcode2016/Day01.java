
package adventofcode2016;

import java.awt.Point;
import java.util.HashSet;
import java.util.Set;

import utils.Input;
/**
 * https://adventofcode.com/2016/day/1
 */
public class Day01 {

    public static void main(String[] args) {
        String steps[] = new Input(2016, 1).strings().get(0).split(", ");
        int dx = 0, dy = 1;
        Point coord = new Point(0, 0);
        Set<Point> track = new HashSet<>();
        track.add(coord);
        Point firstVisited = null;

        for (String s : steps) {
            boolean isRight = s.charAt(0) == 'R';
            int tmp = dx;
            dx = isRight ? dy : -dy;
            dy = isRight ? -tmp : tmp;
            int len = Integer.parseInt(s.substring(1));
            for (int i=0; i<len; ++i) {
                coord = coord.getLocation();
                coord.translate(dx, dy);
                if (track.contains(coord) && firstVisited == null) {
                    firstVisited = coord;
                }
                track.add(coord);
            }
        }
        System.err.println(Math.abs(coord.x) + Math.abs(coord.y));
        System.err.println(Math.abs(firstVisited.x) + Math.abs(firstVisited.y));
    }

}
