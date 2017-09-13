
package adventofcode2016;

import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public final class Utils {

    public static List<String> getStringsFromFile(String file) {
        try {
            URI uri = Utils.class.getResource(file).toURI();
            return Files.readAllLines(Paths.get(uri), StandardCharsets.US_ASCII);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

}
