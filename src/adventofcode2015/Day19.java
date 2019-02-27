package adventofcode2015;

import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/19
 */
public class Day19 {

    static List<String[]> rules;
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
		Input input = new Input(2015, 19);
		rules = input.match("(\\w+) => (\\w+)")
				.map(m -> new String[] {m.group(1), m.group(2)})
				.sorted(Comparator.comparing(s -> -s[1].length()))
				.collect(Collectors.toList());

		List<String> strings = input.strings();
		String start = strings.get(strings.size()-1);
		
		Set<String> molecules = new HashSet<>();
		for (String r[] : rules) {
			for (int i=0; i<start.length(); i++) {
				if (start.substring(i).startsWith(r[0])) {
					String m = start.substring(0, i) + r[1] + start.substring(i + r[0].length());
					if (!molecules.contains(m)) {
						molecules.add(m);
					}
				}
			}
		}
		System.err.println(molecules.size());

		runCounter();
	    shrink(start, 1);
        System.err.println(min);
	}

	static volatile long N = 0;

	static void runCounter() {
		new Thread(() -> {
			try {
				long P = 0;
				for (;;) {
					System.out.println(String.format("%.3e (+%d)", (double)N, N-P));
					P = N;
					Thread.sleep(1000);
				}
			} catch (Exception e) {}
		}).start();
	}

}
