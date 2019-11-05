
package adventofcode2017;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

import utils.Input;

/**
 * https://adventofcode.com/2017/day/20
 */
public class Day20 {

    static long hash(long p[]) {
        return p[0] * 11111 + p[1] * 123456 + p[2];
    }

    public static void main(String[] args) {
        List<String> input = new Input(2017, 20).strings();

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
        
        int minIndex = 0;
        long min = Long.MAX_VALUE;
        for (int j = 0; j < particles.size(); ++j) {
            long p[] = particles.get(j);
            int n = 1000;
            long x = p[0] + p[3] * n + p[6] * n * (n + 1) / 2;
            long y = p[1] + p[4] * n + p[7] * n * (n + 1) / 2;
            long z = p[2] + p[5] * n + p[8] * n * (n + 1) / 2;
            long d = Math.abs(x) + Math.abs(y) + Math.abs(z);
            if (d < min) {
                min = d;
                minIndex = j;
            }
        }
        System.err.println(minIndex);

        List<long[]> removed = new ArrayList<>();
        for (int i=0; i<10000; i++) {
            Map<Long, Integer> hashes = new HashMap<>();
            for (long p[] : particles) {
                p[3] += p[6];
                p[4] += p[7];
                p[5] += p[8];
                p[0] += p[3];
                p[1] += p[4];
                p[2] += p[5];
                long h = hash(p);
                hashes.put(h, hashes.getOrDefault(h, 0) + 1);
            }
            particles.removeIf(p -> hashes.get(hash(p)) > 1);
        }
        System.err.println(particles.size() - removed.size());
    }
}
