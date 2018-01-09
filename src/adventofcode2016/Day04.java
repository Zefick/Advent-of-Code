
package adventofcode2016;

import java.util.Comparator;
import java.util.List;
import java.util.function.ToLongFunction;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

import utils.Input;

public class Day04 {

    // groups: 1 - room name, 2 - id, 3 - checksum
    static Pattern p = Pattern.compile("([-a-z]*)-(\\d+)\\[(\\w{5})\\]");

    static int getID(String room) {
        Matcher m = p.matcher(room);
        m.find();

        int id = Integer.parseInt(m.group(2));
        String name = m.group(1);

        String decripted = name.chars()
                .map(x -> (x == '-') ? ' ' : (x - 'a' + id) % 26 + 'a')
                .mapToObj(x -> String.valueOf((char)x))
                .collect(Collectors.joining());

        ToLongFunction<Integer> counter = c -> name.chars().filter(x -> x == c).count();

        String checksum = name.chars()
                .filter(Character::isAlphabetic)
                .distinct().boxed()
                .sorted(Comparator.comparingLong(counter).reversed()
                            .thenComparing(Comparator.naturalOrder())).limit(5)
                .map(x -> String.valueOf((char)(int)x))
                .collect(Collectors.joining());

        if (decripted.contains("northpole")) {
            System.out.printf("%s %d%n", decripted, id);
        }

        boolean isReal = checksum.equals(m.group(3));
        return isReal ? id : 0;
    }

    public static void main(String[] args) {
        List<String> input = new Input(2016, "input04.txt").strings();
        System.out.println("Sum: " + input.stream().mapToInt(Day04::getID).sum());
    }

}
