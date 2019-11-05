
package adventofcode2017;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import utils.Input;

/**
 * https://adventofcode.com/2017/day/16
 */
public class Day16 {

    static byte[] dance(Object moves[][], byte programs[]) {
        for (Object move[] : moves) {
            if (move[0].equals("s")) {
                int n = (Integer)move[1];
                for (int i=0; i<n; i++) {
                    byte a = programs[15];
                    System.arraycopy(programs, 0, programs, 1, 15);
                    programs[0] = a;
                }
            }
            if (move[0].equals("x")) {
                int a = (Integer)move[1];
                int b = (Integer)move[2];
                byte tmp = programs[a];
                programs[a] = programs[b];
                programs[b] = tmp;
            }
            if (move[0].equals("p")) {
                for (int i=0; i<16; i++) {
                    if (programs[i] == (Byte)move[1]) {
                        programs[i] = (Byte)move[2];
                    } else if (programs[i] == (Byte)move[2]) {
                        programs[i] = (Byte)move[1];
                    }
                }
            }
        }
        return programs;
    }

    static Object[] readMove(String move) {
        Object parts[] = new Object[3];
        parts[0] = move.substring(0, 1);
        if (move.startsWith("s")) {
            parts[1] = Integer.parseInt(move.substring(1));
        } else if (move.startsWith("x")) {
            parts[1] = Integer.parseInt(move.substring(1).split("/")[0]);
            parts[2] = Integer.parseInt(move.substring(1).split("/")[1]);
        } else {
            parts[1] = (byte)move.substring(1).split("/")[0].charAt(0);
            parts[2] = (byte)move.substring(1).split("/")[1].charAt(0);
        }
        return parts;
    }

    public static void main(String[] args) {
        Object moves[][] = Arrays.stream(new Input(2017, 16).strings().get(0).split(","))
                .map(Day16::readMove)
                .toArray(Object[][]::new);

        byte programs[] = "abcdefghijklmnop".getBytes();

        programs = dance(moves, programs);
        System.out.println(new String(programs));

        List<String> cache = new ArrayList<>();
        cache.add(new String(programs));

        for (int i=0; i<1_000_000_000-1; i++) {
            programs = dance(moves, programs);
            if (new String(programs).equals(cache.get(0))) {
                System.out.println(cache.get((999999998-i) % (i+1)));
                break;
            }
            cache.add(new String(programs));
        }
    }
}
