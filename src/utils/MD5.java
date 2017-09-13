
package utils;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5 {

    public static MessageDigest md;

    public static String encode(String s) {
        if (md == null) {
            try {
                md = MessageDigest.getInstance("MD5");
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
            }
        }
        return String.format("%032x", new BigInteger(1, md.digest((s).getBytes())));
    }
}
