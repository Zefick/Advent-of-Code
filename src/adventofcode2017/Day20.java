
package adventofcode2017;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

import utils.Input;

public class Day20 {

    public static void main(String[] args) {
        List<String> input = new Input(2017, "input20.txt").strings();

        List<long[]> particles = new ArrayList<>();
        for (String s : input) {
            try (Scanner sc = new Scanner(s)) {
                long coords[] = new long[9];
                for (int i=0; i<9; i++) {
                    coords[i] = Integer.parseInt(sc.findInLine("-?\\d+"));
                }
                particles.add(coords);
            }
        }
        for (int i=0; i<100000; i++) {
            long min = Long.MAX_VALUE;
            int minIndex = 0;
            Map<Long, Integer> hashes = new HashMap<>();
            for (int j = 0; j < particles.size(); ++j) {
                long p[] = particles.get(j);
                long d = Math.abs(p[0]) + Math.abs(p[1]) + Math.abs(p[2]);
                if (d < min) {
                    min = d;
                    minIndex = j;
                }
                p[3] += p[6];
                p[4] += p[7];
                p[5] += p[8];
                p[0] += p[3];
                p[1] += p[4];
                p[2] += p[5];
                long h = p[0] * 11111 + p[1] * 123456 + p[2];
                hashes.put(h, hashes.getOrDefault(h, 0) + 1);
            }
            particles = particles.stream()
                    .filter(p -> hashes.get(p[0] * 11111 + p[1] * 123456 + p[2]) == 1)
                    .collect(Collectors.toList());
        }
        System.out.println(particles.size());
    }
}
