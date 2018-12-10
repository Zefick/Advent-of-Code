package adventofcode2018;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;

/**
 * https://adventofcode.com/2018/day/9
 */
public class Day09 {

    public static void main(String[] args) {

        int players = 459;
        int maxScore = 71320;

        List<Integer> marbles = new LinkedList<>();
        long[] scores = new long[players];
        marbles.add(0);
        int p = 0;

        ListIterator<Integer> it = marbles.listIterator();
        Runnable printMaxScores = () ->
                System.err.println(Arrays.stream(scores).max().getAsLong());

        game:
        for (int m=1; ; m++) {
            if (m % 23 == 0) {
                scores[p] += m;
                it = advance(marbles, it, -7);
                scores[p] += it.next();
                it.previous();
                it.remove();
            } else {
                it = advance(marbles, it, 2);
                it.add(m);
                it.previous();
            }
            if (m == maxScore) {
                printMaxScores.run();
            } if (m == maxScore * 100) {
                break game;
            }
            p = (p + 1) % players;
        }
        printMaxScores.run();
    }

    static <T> ListIterator<T> advance(List<T> list, ListIterator<T> it, int delta) {
        while (delta != 0) {
            if (delta > 0) {
                if (!it.hasNext()) {
                    it = list.listIterator();
                }
                it.next();
                delta--;
            } else {
                if (!it.hasPrevious()) {
                    it = list.listIterator(list.size());
                }
                it.previous();
                delta++;
            }
        }
        return it;
    }

}
