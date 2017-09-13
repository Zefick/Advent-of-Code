
package adventofcode2016;

import utils.Input;

public class Day02 {

    static char[][] map = {
        { 0,   0,  '1',  0,   0 },
        { 0,  '2', '3', '4',  0 },
        {'5', '6', '7', '8', '9'},
        { 0,  'A', 'B', 'C',  0 },
        { 0,   0,  'D',  0,   0 }
    };

    public static void main(String[] args) {
        int p1[] = {2, 0};
        for (String s : new Input(2016, "input02.txt").strings()) {
            for (int c : s.toCharArray()) {
                int p2[];
                if (c == 'L')      p2 = new int[] {Math.max(0, p1[0]-1), p1[1]};
                else if (c == 'R') p2 = new int[] {Math.min(4, p1[0]+1), p1[1]};
                else if (c == 'U') p2 = new int[] {p1[0], Math.max(0, p1[1]-1)};
                else               p2 = new int[] {p1[0], Math.min(4, p1[1]+1)};
                if (map[p2[1]][p2[0]] != 0) p1 = p2;
            }
            System.out.print(map[p1[1]][p1[0]]);
        }
    }

}
