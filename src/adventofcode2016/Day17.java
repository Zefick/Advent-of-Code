
package adventofcode2016;

import java.util.function.BinaryOperator;

public class Day17 {

    static int h = 0;

    static final BinaryOperator<String> cmp = (s1, s2) -> (s2.length() > s1.length() ? s2 : s1);

    static String findPath(int x, int y, String passcode) {
        if (x == 3 && y ==3) {
            return passcode;
        }

        int hash[] = Utils.getMD5(passcode).chars().limit(4).map(c -> (c>'a' && c<='f') ? 1 : 0).toArray();
        h++;
        String path = passcode;
        if (y > 0 && hash[0] == 1) {
            path = findPath(x, y-1, passcode + 'U');
        }
        if (y < 3 && hash[1] == 1) {
            path = cmp.apply(path, findPath(x, y+1, passcode + 'D'));
        }
        if (x > 0 && hash[2] == 1) {
            path = cmp.apply(path, findPath(x-1, y, passcode + 'L'));
        }
        if (x < 3 && hash[3] == 1) {
            path = cmp.apply(path, findPath(x+1, y, passcode + 'R'));
        }
        return path;
    }

    public static void main(String[] args) {
        String passcode = "pvhmgsws";
        String path = findPath(0, 0, passcode);

        System.out.println(path.length() - passcode.length());
        System.out.println(path.substring(passcode.length()));
        System.out.println(h);
    }

}
