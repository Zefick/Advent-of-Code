
package adventofcode2017;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import utils.Input;

public class Day22 {

    static int hash (int x, int y) {
        return x * 100000 + y;
    }

    enum State {
        CLEAN, WEAKENED, INFECTED, FLAGGED
    }

    public static void main(String[] args) {
        List<String> input = new Input(2017, "input22.txt").strings();

        Map<Integer, State> infected =new HashMap<>();

        int w = input.get(0).length();
        int h = input.size();
        for (int y=0; y<h; ++y) {
            for (int x=0; x<w; ++x) {
                if (input.get(y).charAt(x) == '#') {
                    infected.put(hash(y, x), State.INFECTED);
                }
            }
        }

        int x = w/2, y = h/2;
        int dir[] = {-1, 0};
        int count = 0;

        for (int i=0; i<10000000; ++i) {
            int key = hash(y, x);
            if (infected.containsKey(key)) {
                switch(infected.get(key)) {
                    case FLAGGED:
                        dir = new int[] {-dir[0], -dir[1]};
                        infected.remove(key);
                        break;
                    case INFECTED:
                        dir = new int[] {dir[1], -dir[0]};
                        infected.put(key, State.FLAGGED);
                        break;
                    case WEAKENED:
                        infected.put(key, State.INFECTED);
                        count++;
                        break;
                    default:
                        break;
                }
            } else {
                dir = new int[] {-dir[1], dir[0]};
                infected.put(key, State.WEAKENED);
            }
            x += dir[1];
            y += dir[0];
        }

        System.out.println(count);
    }
}
