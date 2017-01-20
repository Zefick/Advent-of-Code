
package adventofcode2016;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day09 {

    static Pattern p = Pattern.compile("\\((\\d+)x(\\d+)\\)(.)");

    public static void main(String[] args) {
        String input = Utils.getStringsFromFile("input09.txt").get(0);
        System.out.println(decompress(input));
    }

    private static long decompress(String input) {
        long len = 0;
        while (true) {
            Matcher m = p.matcher(input);
            if (!m.find()) {
                len += input.length();
                break;
            } else {
                int a = Integer.parseInt(m.group(1)),
                    b = Integer.parseInt(m.group(2)),
                    c = m.start(3);
                len += decompress(input.substring(c, c + a)) * b;
                input = input.substring(c + a);
            }
        }
        return len;
    }

}
