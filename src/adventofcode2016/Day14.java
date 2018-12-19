package adventofcode2016;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.MD5;

/**
 * https://adventofcode.com/2016/day/14
 */
public class Day14 {

    static String input = "cuanljph";

    static List<String> cache;

    static String getHash(int x, int n) {
        if (x < cache.size()) {
            return cache.get(x);
        }
        String s = input + x;
        for (int i=0; i<=n; i++) {
            s = MD5.encode(s);
        }
        cache.add(s);
        return s;
    }

    public static void main(String[] args) throws Exception {

        Pattern p = Pattern.compile("(.)\\1\\1");
        long t = System.currentTimeMillis();

        for (int k : new int[] {0, 2016}) {
            int n = 0;
            cache = new ArrayList<>();
            loop1:
            for (int i=0;; i++) {
                String hash = getHash(i, k);
                Matcher m = p.matcher(hash);
                if (m.find()) {
                    String c = m.group(1);
                    for (int j=0; j<1000; ++j) {
                        if (getHash(i+j+1, k).contains(c+c+c+c+c)) {
                            System.out.printf("%d %d\n", ++n, i);
                            if (n == 64) {
                                System.err.println(i);
                                break loop1;
                            }
                            break;
                        }
                    }
                }
            }
        }
        System.out.println((System.currentTimeMillis() - t) * 1e-3);
    }

}
