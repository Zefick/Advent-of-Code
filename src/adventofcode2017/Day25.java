
package adventofcode2017;

import java.util.HashSet;
import java.util.Set;

public class Day25 {

    enum State {
        A(1, 1, 1, 0, 1, 5),
        B(0, -1, 1, 1, -1, 2),
        C(1, -1, 3, 0, 1, 2),
        D(1, -1, 4, 1, 1, 0),
        E(1, -1, 5, 0, -1, 3),
        F(1, 1, 0, 0, -1, 4);

        State(int v0, int m0, int s0, int v1, int m1, int s1) {
            val0 = v0; move0 = m0; state0 = s0;
            val1 = v1; move1 = m1; state1 = s1;
        }

        int val0, move0, val1, move1, state0, state1;
    }

    public static void main(String[] args) {

        Set<Integer> tape = new HashSet<>();

        State state = State.A;
        int pos = 0;

        for (int i=0; i<12425180; i++) {
            if (tape.contains(pos)) {
                if (state.val1 == 1) {
                    tape.add(pos);
                } else {
                    tape.remove(pos);
                }
                pos += state.move1;
                state = State.values()[state.state1];
            } else {
                if (state.val0 == 1) {
                    tape.add(pos);
                } else {
                    tape.remove(pos);
                }
                pos += state.move0;
                state = State.values()[state.state0];
            }
        }
        System.out.println(tape.size());
    }
}
