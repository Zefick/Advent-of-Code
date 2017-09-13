
package adventofcode2016;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day07 {

    static Pattern p1 = Pattern.compile("(\\w)(\\w)\\2\\1");

    static boolean checkTLS(String s) {
        String parts[] = s.split("\\[|\\]");
        boolean b = false;
        for (int i=0; i<parts.length; ++i) {
            Matcher m = p1.matcher(parts[i]);
            if (m.find() && !m.group(1).equals(m.group(2))) {
                if (i%2 == 0) {
                    b = true;
                } else {
                    return false;
                }
            }
        }
        return b;
    }

    static Pattern p2 = Pattern.compile("\\w*(\\w)(\\w)\\1\\w*\\[.*\\2\\1\\2\\w*\\]");
    static Pattern p3 = Pattern.compile("\\[\\w*(\\w)(\\w)\\1.*\\]\\w*\\2\\1\\2");

    static boolean checkSSL(String s) {
        Matcher m = p2.matcher(s);
        if (m.find() && !m.group(1).equals(m.group(2))) {
            return true;
        }
        m = p3.matcher(s);
        return m.find() && !m.group(1).equals(m.group(2));
    }

    public static void main(String[] args) {
        List<String> strings = new Input(2016, "input07.txt").strings();

        System.out.println("Supports TLS: "
                + strings.stream().filter(Day07::checkTLS).count());

        System.out.println("Supports SSL: "
                + strings.stream().filter(Day07::checkSSL).count());
    }

}
