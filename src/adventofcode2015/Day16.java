
package adventofcode2015;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day16 {

    public static void main(String[] args) {

        Map<String, Integer> stats = new HashMap<>();
        stats.put("children", 3);
        stats.put("cats", 7);
        stats.put("samoyeds", 2);
        stats.put("pomeranians", 3);
        stats.put("akitas", 0);
        stats.put("vizslas", 0);
        stats.put("goldfish", 5);
        stats.put("trees", 3);
        stats.put("cars", 2);
        stats.put("perfumes", 1);
        int n=0;

        List<String> input = new Input(2015, "input16.txt").strings();
        Pattern p = Pattern.compile(".*?: (\\w+): (\\d+), (\\w+): (\\d+), (\\w+): (\\d+)");

        outer:
        for (String str : input) {
            Matcher m = p.matcher(str);
            m.find();
            ++n;
            for (int i=0; i<3; ++i) {
                String stat = m.group(i*2+1);
                int num = Integer.parseInt(m.group(i*2+2));
                if (stat.equals("cats") || stat.equals("trees")) {
                    if (num <= stats.get(stat)) {
                        continue outer;
                    }
                } else if (stat.equals("pomeranians") || stat.equals("goldfish")) {
                    if (num >= stats.get(stat)) {
                        continue outer;
                    }
                } else if (num != stats.get(stat)) {
                    continue outer;
                }
            }
            System.out.println(n);
        }
    }

}
