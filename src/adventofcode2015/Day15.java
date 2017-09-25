
package adventofcode2015;

import java.util.ArrayList;
import java.util.List;
import java.util.function.IntUnaryOperator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import utils.Input;

public class Day15 {

    public static void main(String[] args) {
        Pattern p = Pattern.compile("([-0-9]+).*?([-0-9]+).*?([-0-9]+).*?([-0-9]+).*?([-0-9]+)");
        List<int[]> stats = new ArrayList<>();
        List<String> input = new Input(2015, "input15.txt").strings();
        for (String ss : input) {
            Matcher m = p.matcher(ss);
            m.find();
            stats.add(IntStream.range(0, 5).map(i -> Integer.parseInt(m.group(i+1))).toArray());
        }
        int parts[] = new int[4];
        IntUnaryOperator op = n -> IntStream.range(0, 4).map(x -> stats.get(x)[n]*parts[x]).sum();
        int max = 0;
        for (int i1=0; i1<=100; ++i1) {
            for (int i2=i1; i2<=100; ++i2) {
                for (int i3=i2; i3<=100; ++i3) {
                    parts[0] = i1;
                    parts[1] = i2 - i1;
                    parts[2] = i3 - i2;
                    parts[3] = 100 - i3;
                    if (op.applyAsInt(4) == 500) {
                        int result = IntStream.range(0, 4)
                                .map(x -> Math.max(0, op.applyAsInt(x)))
                                .reduce((x, y) -> x*y)
                                .getAsInt();
                        max = Math.max(result, max);
                    }
                }
            }
        }
        System.out.println(max);
    }

}
