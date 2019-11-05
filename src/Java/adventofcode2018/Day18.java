package adventofcode2018;

import java.util.Arrays;
import java.util.List;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/18
 */
public class Day18 {

    public static void main(String[] args) {
        int[][] map = new Input(2018, 18).getMap();
        List<Character> states = Arrays.asList('.', '|', '#');
        int h = map.length, w = map[0].length;
        int max = 5000;
        int scores[] = new int[max];
        for (int t=0; t<max ; t++) {
            final int[][] mapCopy = Arrays.stream(map)
                    .map(int[]::clone)
                    .toArray(int[][]::new);
            for (int y=0; y<h; y++) {
                for (int x=0; x<map[y].length; x++) {
                    int fx = x, fy = y;
                    int counts[] = new int[3];
                    Arrays.stream(new int[][] {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}})
                            .map(dir -> new int[] {fx+dir[0], fy+dir[1]})
                            .filter(dir -> dir[0] >= 0 && dir[0] < w && dir[1] >= 0 && dir[1] < h)
                            .forEach(dir -> counts[states.indexOf((char)mapCopy[dir[1]][dir[0]])]++);
                    if (mapCopy[y][x] == '.' && counts[1] >= 3) map[y][x] = '|';
                    if (mapCopy[y][x] == '|' && counts[2] >= 3) map[y][x] = '#';
                    if (mapCopy[y][x] == '#' && (counts[1] == 0 || counts[2] == 0)) map[y][x] = '.';
                }
            }
            int counts[] = new int[2];
            Arrays.stream(map).flatMapToInt(Arrays::stream).forEach(c -> {
                if (c == '|') counts[0]++;
                if (c == '#') counts[1]++;
            });
            scores[t] = counts[0] * counts[1];
        }
        System.err.println(scores[9]);
        for (int t2 = max-2; t2 > 0; t2--) {
            if (scores[t2] == scores[max-1]) {
                int period = max - 1 - t2;
                System.err.println(scores[1000_000_000 % period + 100 * period - 1]);
                break;
            }
        }
    }
}
