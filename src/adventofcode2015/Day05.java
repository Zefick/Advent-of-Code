
package adventofcode2015;

import java.util.List;

import utils.Input;

public class Day05 {

    public static void main(String[] args) {
        List<String> input = new Input(2015, "input05.txt").strings();

        long n1 = input.stream()
                .filter(str -> str.matches(".*[aeiou].*[aeiou].*[aeiou].*"))
                .filter(str -> str.matches(".*(.)\\1.*"))
                .filter(str -> !str.matches(".*(ab|cd|pq|xy).*"))
                .count();
        System.out.println(n1);

        long n2 = input.stream()
                .filter(str -> str.matches(".*(..).*\\1.*"))
                .filter(str -> str.matches(".*(.).\\1.*"))
                .count();
        System.out.println(n2);
    }

}
