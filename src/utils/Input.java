
package utils;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.List;
import java.util.stream.Collectors;

public class Input {

    private final String path;

    public Input(String path) {
         this.path = path;
    }

    public Input(int year, String file) {
         this.path = "/adventofcode" + year + "/" + file;
    }

    private InputStream inputStream() {
        return getClass().getResourceAsStream(path);
    }

    public List<String> strings() {
        return new BufferedReader(new InputStreamReader(inputStream())).lines()
                .collect(Collectors.toList());
    }

}
