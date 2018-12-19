package adventofcode2016;

/**
 * https://adventofcode.com/2016/day/25
 */
public class Day25 {

    static String[] commands = {
        "cpy a d   ",
        "cpy 11 c  ",
        "cpy 231 b ",
        "inc d     ",
        "dec b     ",
        "jnz b -2  ",
        "dec c     ",
        "jnz c -5  ",
        "cpy d a   ",
        "jnz 0 0   ",
        "cpy a b   ",
        "cpy 0 a   ",
        "cpy 2 c   ",
        "jnz b 2   ",
        "jnz 1 6   ",
        "dec b     ",
        "dec c     ",
        "jnz c -4  ",
        "inc a     ",
        "jnz 1 -7  ",
        "cpy 2 b   ",
        "jnz c 2   ",
        "jnz 1 4   ",
        "dec b     ",
        "dec c     ",
        "jnz 1 -4  ",
        "jnz 0 0   ",
        "out b     ",
        "jnz a -19 ",
        "jnz 1 -21 ",
    };

    public static void main(String[] args) {

        for (int i=0; i<1000; i+=1) {
            Assembunny asm = new Assembunny() {
                @Override
                protected void out(String op) {
                    super.out(op);
                    if (output.length() > 50) {
                        stop();
                    }
                }
            };
            asm.setRegisters(i, 0, 0, 0);
            asm.setCommands(commands);
            asm.run();

            String out = asm.getOutput().toString();
            System.out.printf("%5d | %s\n", i, out);

            if (out.matches("^(01)*(0)?$")) {
                System.err.println(i);
                return;
            }
        }
    }

}
