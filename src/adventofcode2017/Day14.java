
package adventofcode2017;

import java.util.Arrays;
import java.util.stream.Collectors;

public class Day14 {

    static void markGroup(byte map[][], int i, int j) {
        map[i][j] = '0';
        if (i > 0   && map[i-1][j] == '1') markGroup(map, i-1, j);
        if (j > 0   && map[i][j-1] == '1') markGroup(map, i, j-1);
        if (i < 127 && map[i+1][j] == '1') markGroup(map, i+1, j);
        if (j < 127 && map[i][j+1] == '1') markGroup(map, i, j+1);
    }

    public static void main(String[] args) throws Exception {
        String input = "ljoxqyyw";
        int sum = 0;
        byte map[][] = new byte[128][];

        for (int i=0; i<128; i++) {
            int hash[] = KnotHash.hashInts(input + "-" + i);
            String line = Arrays.stream(hash)
                    .mapToObj(x -> Integer.toBinaryString(x+256).substring(1))
                    .collect(Collectors.joining());
            sum += line.chars().filter(c -> c == '1').count();
            map[i] = line.getBytes();
        }
        System.out.println(sum);

        int groups = 0;
        for (int i=0; i<128; i++) {
            for (int j=0; j<128; j++) {
                if (map[i][j] == '1') {
                    markGroup(map, i, j);
                    groups++;
                }
            }
        }
        System.out.println(groups);
    }
}
