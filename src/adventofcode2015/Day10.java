
package adventofcode2015;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day10 {

    public static void main(String[] args) {
        Pattern p = Pattern.compile("(.)\\1*");
        String input = "1321131112";
        for (int i=0; i<50; ++i) {
            Matcher m = p.matcher(input);
            StringBuilder output = new StringBuilder();
            while (m.find()) {
                output.append(m.group().length()).append(m.group(1));
            }
            input = output.toString();
        }
        System.out.println(input.length());
    }

}
