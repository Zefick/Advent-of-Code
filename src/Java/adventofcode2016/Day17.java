
package adventofcode2016;

import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;

import utils.MD5;

/**
 * https://adventofcode.com/2016/day/17
 */
public class Day17 {

    static Set<String> solutions = new HashSet<>();

    static void findPath(int x, int y, String passcode) {
        if (x == 3 && y ==3) {
            solutions.add(passcode);
            return;
        }
        int hash[] = MD5.encode(passcode).chars().limit(4)
                .map(c -> (c>'a' && c<='f') ? 1 : 0)
                .toArray();
        if (y > 0 && hash[0] == 1) findPath(x, y-1, passcode + 'U');
        if (y < 3 && hash[1] == 1) findPath(x, y+1, passcode + 'D');
        if (x > 0 && hash[2] == 1) findPath(x-1, y, passcode + 'L');
        if (x < 3 && hash[3] == 1) findPath(x+1, y, passcode + 'R');
    }

    public static void main(String[] args) {
        String passcode = "njfxhljp";
        findPath(0, 0, passcode);
        Comparator<String> comparator = Comparator.comparing(String::length);
        String shortest = solutions.stream().min(comparator).get();
        System.err.println(shortest.substring(passcode.length()));

        String longest = solutions.stream().max(comparator).get();
        System.err.println(longest.length() - passcode.length());
    }

}
