
package adventofcode2016;

import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

import utils.Input;

public class Day08 {

    static final int H = 6, W = 50;
    static byte screen[][] = new byte[H][W];
    static byte buffer[] = new byte[Math.max(W, H)];


    public static void main(String[] args) {
        List<String> seq = new Input(2016, "input08.txt").strings();
        seq.forEach(s -> {
            String parts[] = s.split(" ");
            if (parts[0].equals("rect")) {
                String rect[] = parts[1].split("x");
                int x = Integer.parseInt(rect[0]);
                int y = Integer.parseInt(rect[1]);
                for (int i=0; i<x; i++) {
                    for (int j=0; j<y; ++j) {
                        screen[j][i] = '@';
                    }
                }
            } else {
                int i = Integer.parseInt(parts[2].substring(parts[2].indexOf('=') + 1));
                int j = Integer.parseInt(parts[4]);
                if (parts[1].equals("row")) {
                    for (int k=0; k<W; ++k) buffer[k] = screen[i][(k-j+W) % W];
                    for (int k=0; k<W; ++k) screen[i][k] = buffer[k];
                } else {
                    for (int k=0; k<H; ++k) buffer[k] = screen[(k-j+H) % H][i];
                    for (int k=0; k<H; ++k) screen[k][i] = buffer[k];
                }
            }
        });
        long n = Arrays.stream(screen)
                .mapToLong(line -> IntStream.range(0, W).filter(j -> line[j] != 0).count())
                .sum();

        System.out.println(n);

        Arrays.stream(screen)
                .map(String::new)
                .forEach(System.out::println);
    }

}
