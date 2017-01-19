
package adventofcode2016;

import java.io.FileReader;
import java.io.IOException;
import java.io.LineNumberReader;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;
import java.util.stream.Collectors;

public final class Utils {

    public static MessageDigest md;

    public static String getMD5(String s) {
        if (md == null) {
            try {
                md = MessageDigest.getInstance("MD5");
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
            }
        }
        return String.format("%032x", new BigInteger(1, md.digest((s).getBytes())));
    }

    public static List<String> getStringsFromFile(String file) {
        file = Utils.class.getResource(file).getPath();
        try (LineNumberReader reader = new LineNumberReader(new FileReader(file))) {
            return reader.lines().collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

}
