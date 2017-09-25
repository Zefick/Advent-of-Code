
package adventofcode2015;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.IntSupplier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import utils.Input;

public class Day13 {

    public static void main(String[] args) {
        Pattern p = Pattern.compile(
                "(\\w)\\w+ would (gain|lose) (\\d+) happiness units by sitting next to (\\w)\\w+.");
        int m[][] = new int[9][9];
        List<String> chars = Arrays.asList("ABCDEFGM".split(""));
        List<String> input = new Input(2015, "input13.txt").strings();
        for (String s : input) {
            Matcher matcher = p.matcher(s);
            matcher.find();
            int n = Integer.parseInt(matcher.group(3));
            m[chars.indexOf(matcher.group(1))][chars.indexOf(matcher.group(4))] = matcher.group(2).equals("gain") ? n : -n;
        }
        List<Integer> order = Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8);
        IntSupplier shuffle = () -> {
            Collections.shuffle(order);
            int x = 0;
            for (int j=0; j<9; ++j) {
                int a = order.get(j);
                int b = order.get((j+1)%9);
                x += m[a][b] + m[b][a];
            }
            return x;
        };
        System.out.println(IntStream.generate(shuffle).limit(100000).max().getAsInt());
    }

}
