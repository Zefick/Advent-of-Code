
package adventofcode2017;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import utils.Input;

public class Day21 {

    static byte[][] rotate(byte map[][]) {
        int l = map.length;
        byte res[][] = new byte[l][l];
        for (int i=0; i<l; ++i) {
            for (int j=0; j<l; ++j) {
                res[i][j] = map[j][l-i-1];
            }
        }
        return res;
    }

    static byte[][] flip(byte map[][]) {
        return map.length == 2
                ? new byte[][] {map[1], map[0]}
                : new byte[][] {map[2], map[1], map[0]};
    }

    static int hash(byte map[][]) {
        return Arrays.stream(map).map(String::new)
                .collect(Collectors.joining()).hashCode();
    }

    public static void main(String[] args) {
        List<String> input = new Input(2017, "input21.txt").strings();

        Map<Integer, String> rules = new HashMap<>();

        for (String rule : input) {
            String s[] = rule.split(" => ");
            byte left[] = s[0].getBytes();
            byte map[][] = rule.length() < 30
                    ? new byte[][] {{left[0], left[1]}, {left[3], left[4]}}
                    : new byte[][] {{left[0], left[1], left[2]}, {left[4], left[5], left[6]}, {left[8], left[9], left[10]}};
            rules.put(hash(map), s[1]);
            rules.put(hash(flip(map)), s[1]);
            rules.put(hash(rotate(map)), s[1]);
            rules.put(hash(flip(rotate(map))), s[1]);
            rules.put(hash(rotate(rotate(map))), s[1]);
            rules.put(hash(flip(rotate(rotate(map)))), s[1]);
            rules.put(hash(rotate(rotate(rotate(map)))), s[1]);
            rules.put(hash(flip(rotate(rotate(rotate(map))))), s[1]);
        }

        byte map[][] = {{'.', '#', '.'}, {'.', '.', '#'}, {'#', '#', '#'}};

        for (int i=0; i<22; ++i) {
            int size = map.length;
            int cellSize = 2 + size % 2;
            byte newMap[][] = new byte[size + (size/cellSize)][size + (size/cellSize)];

            for (int x = 0; x < size / cellSize; ++x) {
                for (int y = 0; y < size / cellSize; ++y) {
                    byte cell[][] = new byte[cellSize][cellSize];
                    for (int x1 = 0; x1 < cellSize; x1++) {
                        for (int y1 = 0; y1 < cellSize; y1++) {
                            cell[x1][y1] = map[x*cellSize+x1][y*cellSize+y1];
                        }
                    }
                    byte pattern[] = rules.get(hash(cell)).getBytes();
                    for (int x1 = 0; x1 < cellSize+1; x1++) {
                        for (int y1 = 0; y1 < cellSize+1; y1++) {
                            newMap[x*(cellSize+1)+x1][y*(cellSize+1)+y1] = pattern[x1*(cellSize+2) + y1];
                        }
                    }
                }
            }
            map = newMap;
            int n = 0;
            for (int x = 0; x < map.length; x++) {
                for (int y = 0; y < map.length; y++) {
                    n += map[x][y] == '#' ? 1 : 0;
                }
            }
            System.out.println((i+1) + ": " + n);
        }
    }
}
