
package adventofcode2015;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import utils.Input;

public class Day14 {

    public static void main(String[] args) {
        Pattern p = Pattern.compile("(\\d+).*?(\\d+).*?(\\d+)");
        List<String> input = new Input(2015, "input14.txt").strings();
        List<int[]> stats = new ArrayList<>();
        for (String ss : input) {
            Matcher m = p.matcher(ss);
            m.find();
            stats.add(IntStream.range(0, 3)
                    .map(i -> Integer.parseInt(m.group(i+1))).toArray());
        }
        int n = stats.size();
        int d[] = new int[n];
        int scores[] = new int[n];
        for (int t=1; t<=2503; ++t) {
            for (int j=0; j<n; ++j) {
                int stat[] = stats.get(j);
                int period = stat[1] + stat[2];
                d[j] = (t/period*stat[1] + Math.min(stat[1], t%period)) * stat[0];
            }
            int max = IntStream.of(d).max().getAsInt();
            IntStream.range(0, n)
                .filter(x -> d[x] == max)
                .forEach(x -> scores[x]++);
        }
        System.out.println(IntStream.of(scores).max().getAsInt());
    }

}
