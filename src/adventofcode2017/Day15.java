
package adventofcode2017;

import java.util.stream.IntStream;
import java.util.stream.LongStream;

public class Day15 {

    private static long[] gen(long init, long mul, long mod, int count) {
        return LongStream
                .iterate(init, x -> (x * mul) % 2147483647)
                .filter(x -> x % mod == 0)
                .limit(count)
                .toArray();
    }

    public static void main(String[] args) {
        long A = 679;
        long B = 771;
        {
            long arr1[] = gen(A, 16807, 1, 40_000_000);
            long arr2[] = gen(B, 48271, 1, 40_000_000);
            System.out.println(IntStream.range(0, 40_000_000)
                    .filter(i -> (arr1[i] & 0xFFFF) == (arr2[i] & 0xFFFF))
                    .count());
        }{
            long arr1[] = gen(A, 16807, 4, 5_000_000);
            long arr2[] = gen(B, 48271, 8, 5_000_000);
            System.out.println(IntStream.range(0, 5_000_000)
                    .filter(i -> (arr1[i] & 0xFFFF) == (arr2[i] & 0xFFFF))
                    .count());
        }
    }
}
