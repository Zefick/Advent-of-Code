package adventofcode2015;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/23
 */
public class Day23 {

    static List<String[]> commands = new ArrayList<>();

	public static void main(String[] args) throws IOException {
        new Input(2015, 23)
                .match("(\\w+) ([ab]|[-+0-9]+)(, ([-+0-9]+))?")
                .map(m -> IntStream.range(0, m.groupCount() + 1)
                        .mapToObj(m::group)
                        .toArray(String[]::new))
                .forEach(commands::add);
        
        int reg[]= {0, 0};
		for (int n=0; n>=0 && n<commands.size();) {
		    n = runCmd(n, reg);
		}
        System.err.println(reg[1]);

        reg = new int[] {1, 0};
		for (int n=0; n>=0 && n<commands.size();) {
		    n = runCmd(n, reg);
		}
		System.err.println(reg[1]);
	}

	static int runCmd(final int n, int reg[]) {
		String ss[] = commands.get(n);
		String cmd = ss[1];
		int r = ss[2].equals("a") ? 0 : 1;
        if (ss[4] != null) {
            int offset = Integer.parseInt(ss[4]);
            if ((cmd.equals("jie") && (reg[r] %2 == 0))
                    || cmd.equals("jio") && (reg[r] == 1)) {
                return n + offset;
            }
        } else {
            if (cmd.equals("hlf")) {
                reg[r] /= 2;
            } else if (cmd.equals("tpl")) {
                reg[r] *= 3;
            } else if (cmd.equals("inc")) {
                reg[r] += 1;
            } else if (cmd.equals("jmp")) {
                return n + Integer.parseInt(ss[2]);
            }
        }
        return n+1;
    }

}
