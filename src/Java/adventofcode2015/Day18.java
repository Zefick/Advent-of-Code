
package adventofcode2015;

import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/18
 */
public class Day18 {

    public static void main(String[] args) {
        int[][] data = new Input(2015, 18).getMap();
        boolean map[][] = new boolean[102][102];
        boolean map2[][] = new boolean[102][102];
        for (int k=0; k<=1; k++) {
            int n = 1;
            for (int[] s : data) {
                final int m = n;
                final boolean fMap[][] = map;
                IntStream.range(1, 101).forEach(i -> fMap[m][i] = (s[i-1] == '#'));
                ++n;
            }
            if (k == 1) {
                map[1][1] = map[1][100] = map[100][1] = map[100][100] = true;
            }
            for (int i=0; i<100; ++i) {
                for (int x=1; x<=100; ++x) {
                    for (int y=1; y<=100; ++y) {
                        Boolean nbrs[] = {
                                map[x-1][y-1], map[x-1][y], map[x-1][y+1], map[x][y-1],
                                map[x][y+1], map[x+1][y-1], map[x+1][y], map[x+1][y+1]
                        };
                        long num = Stream.of(nbrs).filter(t -> t).count();
                        map2[x][y] = (num == 2) & map[x][y] | (num == 3);
                    }
                }
                boolean tmp[][] = map2;
                map2 = map;
                map = tmp;
                if (k == 1) {
                    map[1][1] = map[1][100] = map[100][1] = map[100][100] = true;
                }
            }
            int m = 0;
            for (int x=1; x<=100; ++x) {
                for (int y=1; y<=100; ++y) {
                    if (map[x][y]) m++;
                }
            }
            System.err.println(m);
        }
    }

}
