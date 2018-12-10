package adventofcode2018;

import java.util.Arrays;
import java.util.stream.IntStream;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/8
 */
public class Day08 {

    public static void main(String[] args) {
        int[] input = Arrays.stream(new Input(2018, "input08.txt").strings().get(0).split("\\s+"))
                .mapToInt(Integer::parseInt)
                .toArray();

        Node root = new Node(input, 0);

        System.err.println(root.part1());
        System.err.println(root.part2());
    }

    static class Node {
        int[] metadata;
        Node[] child;
        int length;
        Node(int[] input, int index) {
            int n = input[index];
            int m = input[index + 1];
            child = new Node[n];
            int k = index + 2;
            for (int i=0; i<n; i++) {
                child[i] = new Node(input, k);
                k += child[i].length;
            }
            length = k - index + m;
            int k2 = k;
            metadata = IntStream.range(0, m).map(i -> input[k2 + i]).toArray();
        }
        int part1() {
            return Arrays.stream(metadata).sum()
                    + Arrays.stream(child).mapToInt(Node::part1).sum();
        }
        int part2() {
            if (child.length == 0) {
                return Arrays.stream(metadata).sum();
            } else {
                return Arrays.stream(metadata)
                        .filter(i -> i <= child.length)
                        .map(i -> child[i-1].part2())
                        .sum();
            }
        }
    }

}
