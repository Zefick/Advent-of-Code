
package adventofcode2016;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

/**
 * https://adventofcode.com/2016/day/9
 */
public class Day09 {

    static Pattern p = Pattern.compile("\\((\\d+)x(\\d+)\\)");

    public static void main(String[] args) {
        String input = new Input(2016, 9).strings().get(0);
        System.err.println(decompress(input, false));
        System.err.println(decompress(input, true));
    }

    private static long decompress(String input, boolean recursive) {
        long len = 0;
        while (true) {
            Matcher m = p.matcher(input);
            if (!m.find()) {
                len += input.length();
                break;
            } else {
                int a = Integer.parseInt(m.group(1)),
                    b = Integer.parseInt(m.group(2)),
                    c = m.end(2) + 1;
                if (recursive) {
                    len += decompress(input.substring(c, c + a), true) * b;
                } else {
                    len += a * b;
                }
                input = input.substring(c + a);
            }
        }
        return len;
    }

}
