
package utils;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Output {

    static File debugFile;

    public static void result(int part, Object result) {
        System.err.println("Part " + part + ": " + result);
    }

    public static void debug(String output) {
        if (debugFile == null) {
            debugFile = new File("debug" + System.currentTimeMillis());
        }
        try (FileWriter writer = new FileWriter(debugFile, true)) {
            writer.append(output);
        } catch (IOException e) {
            e.printStackTrace();
		}
    }

    public static void main(String[] args) {
        Output.debug("line1");
        Output.debug("line2");
        Output.debug("line3");
    }

}
