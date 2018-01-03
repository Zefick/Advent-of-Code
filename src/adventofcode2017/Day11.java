
package adventofcode2017;

import utils.Input;

public class Day11 {

    public static void main(String[] args) throws Exception {
        String input = new Input(2017, "input11.txt").strings().get(0);

        int x = 0, y = 0;
        int max = 0, steps = 0;
        for (String s : input.split(",")) {
            switch(s) {
                case "nw" : y -= 1; x -= 1; break;
                case "n" : y -= 1; break;
                case "ne" : x += 1; break;
                case "sw" : x -= 1; break;
                case "s" : y += 1; break;
                case "se" : y += 1; x += 1; break;
            }
            steps = (x > 0 ^ y > 0)
                ? steps = Math.abs(x - y)
                : Math.max(Math.abs(x), Math.abs(y));
            max = Math.max(max, steps);
        }
        System.out.println(steps);
        System.out.println(max);
    }
}
