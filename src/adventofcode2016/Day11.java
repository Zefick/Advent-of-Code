
package adventofcode2016;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.stream.IntStream;

public class Day11 {

    // .  . | .  . | .  . | .  . | .  .  ",
    // .  . | .  . | .  . | G  M | G  M  ",
    // .  . | .  M | .  M | .  . | .  .  ",
    // G  M | G  . | G  . | .  . | .  .  "

    static long start  = 0b11111110100000_00000001010000_00000000001111_00000000000000L | (3L << 56);
    static long finish = 0b00000000000000_00000000000000_00000000000000_11111111111111L;

    /**
     * Checks that each of presented chips has a paired generator or there is no other generators on the floor.
     */
    static boolean possible(int f) {
        return (((f & 0b01000000000000) == 0) || ((f & 0b10000000000000) > 0) || ((f & 0b00101010101010) == 0))
            && (((f & 0b00010000000000) == 0) || ((f & 0b00100000000000) > 0) || ((f & 0b10001010101010) == 0))
            && (((f & 0b00000100000000) == 0) || ((f & 0b00001000000000) > 0) || ((f & 0b10100010101010) == 0))
            && (((f & 0b00000001000000) == 0) || ((f & 0b00000010000000) > 0) || ((f & 0b10101000101010) == 0))
            && (((f & 0b00000000010000) == 0) || ((f & 0b00000000100000) > 0) || ((f & 0b10101010001010) == 0))
            && (((f & 0b00000000000100) == 0) || ((f & 0b00000000001000) > 0) || ((f & 0b10101010100010) == 0))
            && (((f & 0b00000000000001) == 0) || ((f & 0b00000000000010) > 0) || ((f & 0b10101010101000) == 0));
    }

    static int getFloor(long map, int e) {
        return (int)(map >> (e*14)) & 0b11111111111111;
    }

    /**
     * Counts number of pairs on each of 4 states on each of first 3 floors and packs it in one <code>long</code> variable.
     * State of 4th floor fully determined by states of floors 1-3 and can be skipped.
     * One hash needs 38 bits (3 * 12 + 2)
     */
    static long hash(long f) {
        long res = (f >> 56) << 2;
        long f2 = f;
        for (int i=0; i<3; i++) {      // floors
            for (int k=0; k<7; k++) {  // pairs
                res += 1 << ((f2 & 3) * 3);
                f2 >>= 2;
            }
            res <<= 12;
        }
        return res;
    }

    static long move(long map, int e1, int e2, long f1, long f2) {
        long l14 = (1 << 14) - 1;
        map &= ~((l14 << (e1*14)) | (l14 << (e2*14)));     // clear both floors
        map = map - ((long)e1 << 56) + ((long)e2 << 56);   // change elevator position
        return map | (f1 << (e1*14)) | (f2 << (e2*14));    // fill new floors
    }

    public static void main(String[] args) {

        // creating a list of moves by enumerating all possible combinations
        int pos[] = IntStream.range(0, 14)
                .flatMap(x -> IntStream.range(x, 14)
                        .filter(y -> (y%2 == x%2) || (x%2==0 && y==x+1))
                        .map(y -> (1 << x) | (1 << y)))
                .toArray();

        HashSet<Long> allMoves = new HashSet<Long>();
        ArrayList<Long> current = new ArrayList<Long>();

        allMoves.add(hash(start));
        current.add(start);

        long t = System.currentTimeMillis();

        // possible floors to move from each floor
        int dirs[][] = {{1}, {0, 2}, {1, 3}, {2}};

        for (int depth = 1; !current.isEmpty(); depth++) {
            ArrayList<Long> next = new ArrayList<Long>();
            for (long map : current) {
                int e = (int)(map >> 56);  // elevator position
                int m = getFloor(map, e);  // current floor
                // loop by possible combinations of carried items
                for (int p : pos) {
                    int f1 = m & ~p;
                    if ((m & p) == p && possible(f1)) {
                        for (int e2 : dirs[e]) {
                            int f2 = getFloor(map, e2) | p;
                            if (!possible(f2)) {
                                continue;
                            }
                            long newmap = move(map, e, e2, f1, f2);
                            long hash = hash(newmap);
                            if (!allMoves.contains(hash)) {
                                if (newmap == finish) {
                                    System.out.println(" * " + depth);
                                }
                                next.add(newmap);
                                allMoves.add(hash);
                            }
                        }
                    }
                }
            }
            current = next;
        }
        System.out.printf("%.3f s.\n", (System.currentTimeMillis() - t) * 1e-3);
    }

}
