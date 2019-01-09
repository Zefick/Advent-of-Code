
package utils;

import java.io.*;
import java.util.*;
import java.util.regex.*;
import java.util.stream.*;

public class Input {

    private final String path;

    public Input(int year, String file) {
        this.path = "input/" + year + "/" + file;
    }

    public Input(int year, int day) {
        this.path = String.format("input/%d/input%02d.txt", year, day);
    }

    public List<String> strings() {
        try (BufferedReader reader = new BufferedReader(new FileReader(new File(path)))) {
            return reader.lines().collect(Collectors.toList());
        } catch (IOException e) {
            return Collections.emptyList();
        }
    }

    public Stream<Matcher> match(String regex) {
        Pattern pattern = Pattern.compile(regex);
        return strings().stream()
                .map(pattern::matcher)
                .filter(Matcher::find);
    }

    public int[][] getMap() {
        return strings().stream()
                .map(s -> s.chars().toArray())
                .toArray(int[][]::new);
    }

}
