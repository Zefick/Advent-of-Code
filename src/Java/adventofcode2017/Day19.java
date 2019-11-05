
package adventofcode2017;

import utils.Input;

/**
 * https://adventofcode.com/2017/day/19
 */
public class Day19 {

    public static void main(String[] args) {
        int map[][] = new Input(2017, 19).getMap();
        int x = 0, y = 0;
        int dx = 0, dy = 1;
        String message = "";
        for (int i=0; i<map.length; i++) {
            if (map[0][i] != ' ') {
                x = i;
                break;
            }
        }
        int steps = 0;
        for (;map[y][x] != ' ';) {
            steps++;
            if (Character.isAlphabetic(map[y][x])) {
                message += Character.toString((char)map[y][x]);
            } else if (map[y][x] == '+') {
                if (map[y-1][x] != ' ' && dy == 0) {
                    dy = -1;
                    dx = 0;
                } else if (map[y+1][x] != ' ' && dy == 0) {
                    dy = 1;
                    dx = 0;
                } else if (map[y][x-1] != ' ' && dx == 0) {
                    dy = 0;
                    dx = -1;
                } else if (map[y][x+1] != ' ' && dx == 0) {
                    dy = 0;
                    dx = 1;
                } else {
                    break;
                }
            }
            x += dx;
            y += dy;
        }
        System.err.println(message);
        System.err.println(steps);
    }
}
