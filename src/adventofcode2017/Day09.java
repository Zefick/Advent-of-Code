
package adventofcode2017;

import utils.Input;

public class Day09 {

    public static void main(String[] args) throws Exception {
        String input = new Input(2017, "input09.txt").strings().get(0);
        System.out.println(input.length());

        input = input.replaceAll("\\!.", "");
        int len = input.length();

        input = input.replaceAll("<.*?>", "<>");
        len -= input.length();

        input = input.replaceAll("<>|,", "");

        int sum = 0, n = 0;
        for (byte c : input.getBytes()) {
            if (c == '{') {
                n++;
                sum += n;
            } else {
                n--;
            }
        }
        System.out.println(sum);
        System.out.println(len);
    }
}
