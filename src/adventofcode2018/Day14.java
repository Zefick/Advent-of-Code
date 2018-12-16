package adventofcode2018;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * https://adventofcode.com/2018/day/14
 */
public class Day14 {

    static String getScores(List<Integer> recipes, int start, int len) {
        return IntStream.range(start, start + len)
                .map(recipes::get)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining());
    }

    public static void main(String[] args) {
        String inputStr = "290431";
        int input = Integer.parseInt(inputStr);
        List<Integer> recipes = new ArrayList<>();
        recipes.add(3);
        recipes.add(7);
        int elf1 = 0, elf2 = 1;
        boolean part1 = false;
        int inputLen = inputStr.length();

        loop:
        for (;;) {
            int sum = recipes.get(elf1) + recipes.get(elf2);
            if (sum < 10) {
                recipes.add(sum);
            } else {
                recipes.add(1);
                recipes.add(sum % 10);
            }
            elf1 = (elf1 + recipes.get(elf1) + 1) % recipes.size();
            elf2 = (elf2 + recipes.get(elf2) + 1) % recipes.size();
            if (!part1 && recipes.size() >= input + 10) {
                String result = getScores(recipes, input, 10);
                System.err.println(result);
                part1 = true;
            }
            for (int i=0; i<=sum/10 && recipes.size() > inputLen; i++) {
                String scores = getScores(recipes, recipes.size() - inputLen - i, inputLen);
                if (scores.startsWith(inputStr)) {
                    System.err.println(recipes.size() - inputLen - i);
                    break loop;
                }
            }
        }

    }
}
