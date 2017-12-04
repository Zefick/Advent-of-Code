package adventofcode2015;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import utils.Input;

public class Day23 {

    static int reg[]= {1, 0};
    static List<String[]> commands = new ArrayList<>();

	public static void main(String[] args) throws IOException {
        //                          1      2              3  4
        Pattern p = Pattern.compile("(\\w+) ([ab]|[-+0-9]+)(, ([-+0-9]+))?");

        new Input(2015, "input23.txt").strings().stream()
                .map(p::matcher)
                .filter(Matcher::find)
                .map(m -> IntStream.range(0, m.groupCount()+1)
                        .mapToObj(m::group)
                        .toArray(String[]::new))
                .forEach(commands::add);

		for (int n=0; n>=0 && n<commands.size();) {
		    n = runCmd(n);
		}
		System.out.println(Arrays.toString(reg));
	}

	static int runCmd(final int n) {
		System.out.println(Arrays.toString(reg));
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
