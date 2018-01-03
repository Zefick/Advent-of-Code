package adventofcode2017;

import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class KnotHash {

    public static int oneRound(int data[], int lengths[], int pos, int skip) {
        for (int x : lengths) {
            int last = pos + x - 1;
            for (int i=0; i<x/2; i++) {
                int tmp = data[(pos+i)%256];
                data[(pos+i)%256] = data[(last-i)%256];
                data[(last-i)%256] = tmp;
            }
            pos += x + skip;
            skip++;
        }
        return pos;
    }

    public static int[] hashInts(String input) {
        int lengths[] = IntStream.concat(input.chars(), IntStream.of(17, 31, 73, 47, 23)).toArray();
        int data[] = IntStream.range(0, 256).toArray();

        int pos = 0;
        for (int j=0; j<64; j++) {
            pos = oneRound(data, lengths, pos, lengths.length * j);
        }

        return IntStream.range(0, 16)
                .map(i -> IntStream.range(i*16, i*16+16).reduce(0, (a, b) -> a ^ data[b]))
                .toArray();
    }

    public static String hashString(String input) {
        return Arrays.stream(hashInts(input))
                .mapToObj(i -> String.format("%02x", i))
                .collect(Collectors.joining());
    }

}
