
package utils;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

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

    public int[][] getMap() {
        return strings().stream()
                .map(s -> s.chars().toArray())
                .toArray(int[][]::new);
    }

}
