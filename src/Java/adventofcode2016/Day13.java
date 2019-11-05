package adventofcode2016;

import java.awt.Point;

import adventofcode2016.PathFinder.PathFinder2D;

/**
 * https://adventofcode.com/2016/day/13
 */
public class Day13 {

    static int input = 1352;

    static boolean isEmpty(Point p) {
        int x = p.x, y = p.y;
        return x >= 0 && y >= 0 &&
                Integer.bitCount((x+3)*x + (2*x + y + 1)*y + input) % 2 == 0;
    }

    public static void main(String[] args) {

        PathFinder2D pf = new PathFinder2D();
        pf.setMovePredicate(Day13::isEmpty);

        pf.setFinishCallback(() -> System.out.println("path length: " + pf.getSteps()));

        pf.setStepCallback(steps -> {
            if (steps == 50) {
                System.out.println("cells number: " + pf.getVisited().size());
            } else if (steps > 100) {
                pf.stop();
            }
        });

        pf.run(new Point(1, 1), new Point(31, 39));
    }

}
