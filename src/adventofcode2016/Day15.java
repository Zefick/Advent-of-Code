package adventofcode2016;

import java.io.IOException;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day15 {

    static int data[][] = {
        {17, 1}, {7, 0}, {19, 2}, {5, 0}, {3, 0}, {13, 5}, {11, 0}
    };

    static int bruteforce() {
        return IntStream.iterate(1, x -> x+1)
                .filter(t -> Stream.of(data).allMatch(d -> (t + d[1]) % d[0] == 0))
                .findFirst().getAsInt();
    }

    /**
     * finds single equivalent of two disks
     */
    static int[] zip(int a[], int b[]) {
        int t = a[0] - a[1] % a[0];
        while ((b[1] + t) % b[0] != 0) {
            t += a[0];
        }
        return new int[] {a[0]*b[0], a[0]*b[0] - t};
    }

    public static void main(String[] args) throws IOException {
        IntStream.range(0, data.length).forEach(i -> data[i][1] += i);
        Stream.of(data).reduce(Day15::zip).ifPresent(x -> System.out.println(x[0]-x[1]));
    }

}
