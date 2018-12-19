package adventofcode2016;

import java.util.stream.Stream;

/**
 * https://adventofcode.com/2016/day/16
 */
public class Day16 {

    static String checksum(String s) {
        StringBuilder sb = new StringBuilder(s.length() / 2);
        for (int i=0; i<s.length()/2; ++i) {
            sb.append(s.charAt(i*2) == s.charAt(i*2+1) ? '1' : '0');
        }
        return sb.toString();
    }

    static String mirror(String s) {
        char cs[] = s.toCharArray();
        StringBuilder sb = new StringBuilder(s.length() * 2 + 1);
        for (int i=s.length()-1; i>=0; --i) {
            sb.append(cs[i] == '1' ? '0' : '1');
        }
        return s + "0" + sb;
    }

    public static void main(String[] args) {
        String input = "10010000000110000";
        int len1 = 272, len2 = 35651584;

        input = Stream.iterate(input, Day16::mirror)
                .filter(x -> x.length() >= len2).findFirst().get();

        Stream.iterate(input.substring(0, len1), Day16::checksum)
                .filter(x -> x.length() % 2 == 1).findFirst().ifPresent(System.err::println);

        Stream.iterate(input.substring(0, len2), Day16::checksum)
                .filter(x -> x.length() % 2 == 1).findFirst().ifPresent(System.err::println);
    }
}
