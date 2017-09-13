
package adventofcode2015;

import java.util.stream.IntStream;

import utils.MD5;

public class Day04 {

    public static void main(String[] args) {
        String input = "ckczppom";
        int n = IntStream.iterate(1, x -> x+1)
            .filter(x -> MD5.encode(input + x).startsWith("000000"))
            .findFirst().getAsInt();
        System.out.println(n);
    }

}
