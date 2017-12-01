package adventofcode2015;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day19 {

    static List<String[]> rules = new ArrayList<>();
    static int min = 1000;

    static void shrink(String start, int depth) {
    	if (depth >= min) {
    		return;
    	}
        for (String[] rule : rules) {
            for (int s=0;; s++) {
            	s = start.indexOf(rule[1], s);
            	if (s < 0) break;
                String replaced = start.substring(0, s) + rule[0] + start.substring(s+rule[1].length());
                ++N;
                if (replaced.equals("e")) {
                	min = depth;
                	System.err.println(min);
                	return;
                }
                shrink(replaced, depth+1);
            }
        }
    }

	public static void main(String[] args) throws Exception {
		runCounter();
	    Pattern p = Pattern.compile("(\\w+) => (\\w+)");
	    List<String> input = new Input(2015, "input19.txt").strings();
	    int i=0;
	    for (;; i++) {
	        String s = input.get(i);
	        Matcher m = p.matcher(s);
	        if (!m.find()) break;
	        rules.add(new String[] {m.group(1), m.group(2)});
	    }
        rules.sort(Comparator.comparing(s -> -s[1].length()));
	    String start = input.get(i+1);
	    shrink(start, 1);
        System.err.println(min);
	}

	static volatile long N = 0;

	static void runCounter() {
		new Thread(() -> {
			try {
				long P = 0;
				for (;;) {
					System.out.println(String.format("%.3e (%d)", (double)N, N-P));
					P = N;
					Thread.sleep(1000);
				}
			} catch (Exception e) {}
		}).start();
	}

}
