
package adventofcode2017;

/**
 * https://adventofcode.com/2017/day/17
 */
public class Day17 {

    static class SpinNode {
        int value;
        SpinNode next;
    }

    public static void main(String[] args) {
        int input = 355;

        SpinNode root = new SpinNode();
        root.value = 0;
        root.next = root;

        for (int i=1; i<=2017; i++) {
            for (int j=0; j<input; j++) {
                root = root.next;
            }
            SpinNode newRoot = new SpinNode();
            newRoot.value = i;
            newRoot.next = root.next;
            root.next = newRoot;
            root = newRoot;
        }
        System.out.println(root.next.value);

        int next = 0, pos = 0;
        for (int i=1; i<=50_000_000; i++) {
            pos = (pos + input) % i + 1;
            if (pos == 1) {
                next = i;
            }
        }
        System.out.println(next);
    }
}
