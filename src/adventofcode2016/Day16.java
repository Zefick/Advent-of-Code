package adventofcode2016;

import java.util.stream.Stream;

public class Day16 {

    static int len = 35651584;
    static StringBuilder sb = new StringBuilder(len);

    static String checksum(String s) {
        sb.setLength(0);
        for (int i=0; i<s.length()/2; ++i) {
            sb.append(s.charAt(i*2) == s.charAt(i*2+1) ? '1' : '0');
        }
        return sb.toString();
    }

    static String mirror(String s) {
        char cs[] = s.toCharArray();
        sb.setLength(0);
        for (int i=s.length()-1; i>=0; --i) {
            sb.append(cs[i] == '1' ? '0' : '1');
        }
        return s + "0" + sb;
    }

    public static void main(String[] args) {
        String input = Stream.iterate("01000100010010111", Day16::mirror)
            .filter(x -> x.length() >= len).findFirst().get();

        Stream.iterate(checksum(input.substring(0, len)), Day16::checksum)
            .filter(x -> x.length() % 2 == 1).findFirst().ifPresent(System.out::println);
    }
}
