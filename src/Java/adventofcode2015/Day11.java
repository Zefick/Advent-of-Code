
package adventofcode2015;

import java.math.BigInteger;
import java.util.function.Function;
import java.util.function.IntUnaryOperator;
import java.util.function.Predicate;
import java.util.regex.Pattern;
import java.util.stream.Stream;

/**
 * https://adventofcode.com/2015/day/11
 */
public class Day11 {

    public static void main(String[] args) {
        Pattern p1 = Pattern.compile("((.)\\2).*((.)\\4)");
        Pattern p2 = Pattern.compile("((.)\\2).*(\\2\\2)");
        Pattern p3 = Pattern.compile("[iol]");
        Pattern p4 = Pattern.compile("abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz");

        Function<IntUnaryOperator, Function<String, String>> transform
                = op -> (str -> new String(str.chars().map(op).toArray(), 0, str.length()));

        Function<String, String>
                op1 = transform.apply(i -> (i>'j') ? i-10 : ('0'+(i-'a'))),
                op2 = transform.apply(i -> (i<='9') ? ('a'+(i-'0')) : i+10);

        Predicate<String> isGood = x -> p1.matcher(x).find()
                && !p2.matcher(x).find()
                && !p3.matcher(x).find()
                && p4.matcher(x).find();

        String input = "vzbxkghb";
        BigInteger b = new BigInteger(op1.apply(input), 26);
        Stream.iterate(b, x -> x.add(BigInteger.ONE))
                .map(x -> op2.apply(x.toString(26)))
                .filter(isGood)
                .limit(2)
                .forEach(System.err::println);
    }

}
