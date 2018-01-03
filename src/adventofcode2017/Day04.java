
package adventofcode2017;

import java.util.Arrays;
import java.util.List;

import utils.Input;

public class Day04 {

    static boolean check1(String[] arr) {
        return Arrays.stream(arr).distinct().count() == arr.length;
    }

    static boolean check2(String[] arr) {
        return Arrays.stream(arr)
                .map(s -> Arrays.toString(s.chars().sorted().toArray()))
                .distinct().count() == arr.length;
    }

    public static void main(String[] args) throws Exception {
        List<String> input = new Input(2017, "input04.txt").strings();
        String arrays[][] = input.stream().map(s -> s.split("\\s+")).toArray(String[][]::new);
        System.out.println(Arrays.stream(arrays).filter(Day04::check1).count());
        System.out.println(Arrays.stream(arrays).filter(Day04::check2).count());
    }

}
