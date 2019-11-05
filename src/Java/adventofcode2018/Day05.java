package adventofcode2018;

import java.util.Comparator;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/5
 */
public class Day05 {
    
    public static void main(String[] args) {
        String input = new Input(2018, 5).strings().get(0);
        
        String input0 = react(input);
        System.err.println(input0.length());
        
        int min = IntStream.range('a', 'z')
            .mapToObj(c -> react(input0.replaceAll("(?i)" + (char)c, "")).length())
            .min(Comparator.naturalOrder()).get();

        System.err.println(min);
    }

    private static String react(String input) {
        outer:
        while (true) {
            for (int i=0; i<input.length()-1; i++) {
                char c1 = input.charAt(i);
                char c2 = input.charAt(i+1);
                if ((Character.toLowerCase(c1) == Character.toLowerCase(c2)) &&
                        (Character.isLowerCase(c1) ^ Character.isLowerCase(c2))) {
                    input = input.substring(0, i) + input.substring(i+2);
                    continue outer;
                }
            }
            break;
        }
        return input;
    }

}
