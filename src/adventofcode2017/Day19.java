
package adventofcode2017;

import java.util.List;

import utils.Input;

public class Day19 {

    public static void main(String[] args) {
        List<String> input = new Input(2017, "input19.txt").strings();

        byte map[][] = input.stream().map(s -> s.getBytes()).toArray(byte[][]::new);
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

        for (;;) {
            steps++;
            System.out.println(steps);
            if (Character.isAlphabetic(map[y][x])) {
                message += Character.toString((char)map[y][x]);
                System.out.println(message);
            } else if (map[y][x] == '+') {
                if (map[y-1][x] != ' ' && dy != 1) {
                    dy = -1;
                    dx = 0;
                } else if (map[y+1][x] != ' ' && dy != -1) {
                    dy = 1;
                    dx = 0;
                } else if (map[y][x-1] != ' ' && dx != 1) {
                    dy = 0;
                    dx = -1;
                } else if (map[y][x+1] != ' ' && dx != -1) {
                    dy = 0;
                    dx = 1;
                } else {
                    break;
                }
            }
            x += dx;
            y += dy;
        }
        System.out.println(message);
    }
}
