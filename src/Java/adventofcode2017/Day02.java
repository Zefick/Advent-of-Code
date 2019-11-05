
package adventofcode2017;

import java.util.Arrays;
import java.util.List;

import utils.Input;

/**
 * https://adventofcode.com/2017/day/2
 */
public class Day02 {

    public static void main(String[] args) throws Exception {
        List<String> input = new Input(2017, 2).strings();

        int sum1 = 0, sum2 = 0;
        for (String s : input) {
            int vals[] = Arrays.stream(s.split("\\s+")).mapToInt(Integer::parseInt).toArray();
            sum1 += Arrays.stream(vals).max().getAsInt() - Arrays.stream(vals).min().getAsInt();
            for (int i=0; i<vals.length; ++i) {
                for (int j=0; j<vals.length; ++j) {
                    if (i != j && vals[i] % vals[j] == 0) {
                        sum2 += vals[i] / vals[j];
                        break;
                    }
                }
            }
        }
        System.out.println(sum1);
        System.out.println(sum2);
    }

}
