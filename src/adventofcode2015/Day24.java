package adventofcode2015;

import java.util.Random;
import java.util.function.BiConsumer;
import java.util.function.IntToLongFunction;
import java.util.stream.LongStream;

public class Day24 {

    public static void main(String[] args) {
        long mas[] = {1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53,
                59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113};
        long third = LongStream.of(mas).sum() / 3;
        System.out.println(third);
        BiConsumer<Integer, Integer> swap = (i, j) -> {
            long tmp = mas[j];
            mas[j] = mas[i];
            mas[i] = tmp;
        };
        IntToLongFunction calcQuantum = j -> LongStream.of(mas).limit(j).reduce((a, b) -> a*b).getAsLong();
        int success = 0;
        int min1 = 100;
        long min2 = 0;
        Random rnd = new Random();
        long t = System.currentTimeMillis();
        for (int i=0; i<100_000_000; ++i) {
            swap.accept(rnd.nextInt(mas.length), rnd.nextInt(mas.length));
            int sum = 0;
            int j = 0;
            for (; j<mas.length && sum<third; ++j) {
                sum += mas[j];
            }
            if (sum == third) {
                ++success;
                if (j < min1) {
                    min1 = j;
                    min2 = calcQuantum.applyAsLong(j);
                    System.out.println(min2);
                } else if (j == min1) {
                    long q = calcQuantum.applyAsLong(j);
                    if (q < min2) {
                        min2 = q;
                        System.out.println(q);
                    }
                }
            }
        }
        System.out.println("time: " + (System.currentTimeMillis() - t));
        System.out.println(success);
        System.out.println(min1);
        System.out.println(min2);
    }

}
