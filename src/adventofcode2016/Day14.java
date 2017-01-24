package adventofcode2016;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day14 {

    static String id = "ihaygndm";

    static List<String> cache = new ArrayList<>();

    static String getHash(int x) {
        if (x < cache.size()) {
            return cache.get(x);
        }
        String s = id + x;
        for (int i=0; i<=2016; i++) {
            s = Utils.getMD5(s);
        }
        cache.add(s);
        return s;
    }

    public static void main(String[] args) throws Exception {

        Pattern p = Pattern.compile("(.)\\1\\1");
        int n = 0;

        long t = System.currentTimeMillis();

        loop1:
        for (int i=0;; i++) {
            String hash = getHash(i);
            Matcher m = p.matcher(hash);
            if (m.find()) {
                String c = m.group(1);
                for (int j=1; j<=1000; ++j) {
                    if (getHash(i+j).contains(c+c+c+c+c)) {
                        System.out.println(++n);
                        if (n == 64) {
                            System.out.println(i);
                            break loop1;
                        }
                    }
                }
            }
        }
        System.out.println((System.currentTimeMillis() - t) * 1e-3);
    }

}
