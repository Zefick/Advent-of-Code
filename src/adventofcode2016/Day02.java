
package adventofcode2016;

import utils.Input;

/**
 * https://adventofcode.com/2016/day/2
 */
public class Day02 {

    static char[][] map1 = {
        {'1', '2', '3'},
        {'4', '5', '5'},
        {'7', '8', '9'},
    };

    static char[][] map2 = {
        { 0,   0,  '1',  0,   0 },
        { 0,  '2', '3', '4',  0 },
        {'5', '6', '7', '8', '9'},
        { 0,  'A', 'B', 'C',  0 },
        { 0,   0,  'D',  0,   0 }
    };

    public static void main(String[] args) {
        handleMap(map1, 1, 1);
        handleMap(map2, 0, 2);
    }

    private static void handleMap(char[][] map, int x, int y) {
        int p1[] = {y, x};
        String result = "";
        for (String s : new Input(2016, 2).strings()) {
            for (int c : s.toCharArray()) {
                int p2[];
                if (c == 'L')      p2 = new int[] {Math.max(0, p1[0]-1), p1[1]};
                else if (c == 'R') p2 = new int[] {Math.min(map[0].length-1, p1[0]+1), p1[1]};
                else if (c == 'U') p2 = new int[] {p1[0], Math.max(0, p1[1]-1)};
                else               p2 = new int[] {p1[0], Math.min(map[0].length-1, p1[1]+1)};
                if (map[p2[1]][p2[0]] != 0) p1 = p2;
            }
            result += map[p1[1]][p1[0]];
        }
        System.err.println(result);
    }

}
