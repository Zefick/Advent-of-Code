package adventofcode2018;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/13
 */
public class Day13 {

    static class Cart {
        static int dirs[][] = {
            {1, 0, 3, 1}, {0, 1, 2, 0}, {-1, 0, 1, 3}, {0, -1, 0, 2}
        };
        int x, y, dir, nextTurn = -1;
        Cart(int x, int y, int dir) {
            this.x = x;
            this.y = y;
            this.dir = dir;
        }
        void move(int path) {
            if (path == '+') {
                dir = (dir + nextTurn + 4) % 4;
                nextTurn = (nextTurn + 2) % 3 - 1;  // -1 -> 0 -> 1
            } else if (path == '/') {
                dir = dirs[dir][2];
            } else if (path == '\\') {
                dir = dirs[dir][3];
            }
            x += dirs[dir][0];
            y += dirs[dir][1];
        }
    }

    public static void main(String[] args) {
        int track[][] = new Input(2018, 13).getMap();
        int h = track.length;
        int w = track[0].length;
        List<Cart> carts = new ArrayList<>();
        for (int i=0; i<h; i++) {
            for (int j=0; j<w; j++) {
                int c = track[i][j];
                if (c == '>') carts.add(new Cart(j, i, 0));
                else if (c == 'v') carts.add(new Cart(j, i, 1));
                else if (c == '<') carts.add(new Cart(j, i, 2));
                else if (c == '^') carts.add(new Cart(j, i, 3));
            }
        }
        List<Cart> cartsToRemove = new ArrayList<>();
        race:
        for (;;) {
            carts.sort(Comparator.comparing(c -> c.y*1000 + c.x));
            for (Cart c : carts) {
                c.move(track[c.y][c.x]);
                for (Cart c2 : carts) {
                    if (c != c2 && c.x == c2.x && c.y == c2.y) {
                        if (cartsToRemove.isEmpty()) {
                            System.err.println(c.x + "," + c.y);
                        }
                        cartsToRemove.add(c);
                        cartsToRemove.add(c2);
                        break;
                    }
                }
            }
            carts.removeAll(cartsToRemove);
            if (carts.size() == 1) {
                System.err.println(carts.get(0).x + "," + carts.get(0).y);
                break race;
            }
        }
    }
}
