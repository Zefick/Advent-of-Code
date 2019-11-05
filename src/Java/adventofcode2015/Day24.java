package adventofcode2015;

import java.util.Random;
import java.util.function.BiConsumer;
import java.util.stream.LongStream;

/**
 * https://adventofcode.com/2015/day/24
 */
public class Day24 {

    public static void main(String[] args) {
        long mas[] = {1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53,
                59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113};
        BiConsumer<Integer, Integer> swap = (i, j) -> {
            long tmp = mas[j];
            mas[j] = mas[i];
            mas[i] = tmp;
        };
        Random rnd = new Random();
        for (int n = 3; n <= 4; ++n) {
            long weight = LongStream.of(mas).sum() / n;
            int min1 = 100;
            long min2 = 0;
            for (int i=0; i<10_000_000; ++i) {
                int k = mas.length / n;
				swap.accept(rnd.nextInt(k), k + rnd.nextInt(mas.length - k));
                int sum = 0;
                int j = 0;
                for (; j<mas.length && sum<weight; ++j) {
                    sum += mas[j];
                }
                if (sum == weight) {
                    long q = LongStream.of(mas).limit(j).reduce((a, b) -> a*b).getAsLong();
                    if (j < min1 || j == min1 && q < min2) {
                        min1 = j;
                        min2 = q;
                    }
                }
            }
            System.err.println(min2);
        }
    }

}
