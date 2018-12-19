
package adventofcode2016;

import java.io.IOException;

/**
 * https://adventofcode.com/2016/day/12
 */
public class Day12 {

    static String[] commands = {
        "cpy 1 a   ",
        "cpy 1 b   ",
        "cpy 26 d  ",
        "jnz c 2   ",
        "jnz 1 5   ",
        "cpy 7 c   ",
        "inc d     ",
        "dec c     ",
        "jnz c -2  ",
        "cpy a c   ",
        "inc a     ",
        "dec b     ",
        "jnz b -2  ",
        "cpy c b   ",
        "dec d     ",
        "jnz d -6  ",
        "cpy 13 c  ",
        "cpy 14 d  ",
        "inc a     ",
        "dec d     ",
        "jnz d -2  ",
        "dec c     ",
        "jnz c -5  "
    };

    public static void main(String[] args) throws IOException {
        Assembunny asm = new Assembunny();
        asm.setRegisters(0, 0, 0, 0);
        asm.setCommands(commands);
        asm.run();
        System.err.println(asm.getRegisters()[0]);

        asm = new Assembunny();
        asm.setRegisters(0, 0, 1, 0);
        asm.setCommands(commands);
        asm.run();
        System.err.println(asm.getRegisters()[0]);
    }

}
