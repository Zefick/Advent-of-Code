
package adventofcode2017;

import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day10 {

    public static void main(String[] args) throws Exception {
        String input = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216";
        
        int data[] = IntStream.range(0, 256).toArray();
        int lengths[] = Stream.of(input.split(",")).mapToInt(Integer::parseInt).toArray();

        KnotHash.oneRound(data, lengths, 0, 0);
        System.out.println(data[0] * data[1]);

        System.out.println(KnotHash.hashString(input));
    }
}
