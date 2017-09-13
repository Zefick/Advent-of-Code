
package adventofcode2015;

import utils.Input;

public class Day01 {

    public static void main(String[] args) throws Exception {
        String input = new Input(2015, "input01.txt").strings().get(0);
        int depth = 0, i = 1;
        for (byte b : input.getBytes()) {
            depth += b == '(' ? 1 : -1;
            if (depth == -1) {
                System.out.println(i);
                break;
            }
            i++;
        }
    }

}
