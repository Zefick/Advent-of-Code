package adventofcode2018;

import java.util.Comparator;
import java.util.List;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/2
 */
public class Day02 {

    public static void main(String[] args) {
        List<String> input = new Input(2018, "input02.txt").strings();
        input.sort(Comparator.naturalOrder());
        
        int _2 = 0, _3 = 0;
        for (String s : input) {
            boolean b2 = false, b3 = false;
            for (char c='a'; c<='z'; c++) {
                String s1 = s.replace(Character.toString(c), "");
                if (s.length() - s1.length() == 2 && !b2) {
                    _2++;
                    b2 = true;
                } else if (s.length() - s1.length() == 3 && !b3) {
                    _3++;
                    b3 = true;
                }
                s = s1;
            }
        }
        System.err.printf("%d %d %d\n", _2, _3, _2*_3);
        
        outer:
        for (int i=0; i< input.size()-1; i++) {
            String s1 = input.get(i);
            String s2 = input.get(i+1);
            for (int j=0; j<s1.length()-1; j++) {
                String sub1 = s1.substring(0, j) + s1.substring(j+1);
                String sub2 = s2.substring(0, j) + s2.substring(j+1);
                if (sub1.equals(sub2)) {
                    System.err.println(sub1);
                    break outer;
                }
            }
        }
        
    }

}
