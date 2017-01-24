
package adventofcode2016;

import java.io.IOException;

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
        "cpy 19 c  ",
        "cpy 11 d  ",
        "inc a     ",
        "dec d     ",
        "jnz d -2  ",
        "dec c     ",
        "jnz c -5  "
    };

    public static void main(String[] args) throws IOException {
        Assembunny asm = new Assembunny();
        asm.setRegisterss(0, 0, 1, 0);
        asm.setCommands(commands);
        asm.run();
        System.out.println(asm.getRegisters()[0]);
    }

}
