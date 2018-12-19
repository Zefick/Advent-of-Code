package adventofcode2016;

import java.util.regex.Pattern;

public class Assembunny {

    protected String[] commands;
    protected int registers[] = {0, 0, 0, 0};
    protected int ptr = 0;

    protected final StringBuilder output = new StringBuilder();

    public void run() {
        while (ptr < commands.length) {
            String operands[] = commands[ptr].split(" ");
            if (operands[0].startsWith("cpy")) {
                cpy(operands[1], operands[2]);
            } else if (operands[0].startsWith("inc")) {
                inc(operands[1]);
            } else if (operands[0].startsWith("dec")) {
                dec(operands[1]);
            } else if (operands[0].startsWith("jnz")) {
                jnz(operands[1], operands[2]);
            } else if (operands[0].startsWith("tgl")) {
                tgl(operands[1]);
            } else if (operands[0].startsWith("out")) {
                out(operands[1]);
            }
        }
    }

    public StringBuilder getOutput() {
        return output;
    }

    public void setRegisters(int a, int b, int c, int d) {
        registers = new int[] {a, b, c, d};
    }

    public int[] getRegisters() {
        return registers;
    }

    public void setCommands(String[] cmds) {
        commands = cmds;
    }

    protected void stop() {
        ptr = commands.length;
    }

    static final Pattern isReg = Pattern.compile("[a-d]");

    private int getValue(String s) {
        return (isReg.matcher(s).find())
            ? registers[s.charAt(0) - 'a']
            : Integer.parseInt(s);
    }

    protected void tgl(String op) {
        int offset = getValue(op);
        int ptr2 = ptr + offset;
        if (ptr2 >= 0 && ptr2 < commands.length) {
            String comm2;
            String operands2[] = commands[ptr2].split(" ");
            if (operands2.length == 2) {
                if (operands2[0].equals("inc")) {
                    comm2 = "dec ";
                } else if (operands2[0].equals("dec")
                        || (operands2[ptr2].equals("tgl") && operands2[1].matches("\\D"))) {
                    comm2 = "inc ";
                } else {
                    ptr++;
                    return;
                }
                comm2 += operands2[1];
            } else {
                if (operands2[0].equals("jnz") && operands2[2].matches("\\D")) {
                    comm2 = "cpy ";
                } else if (!operands2[0].equals("jnz")) {
                    comm2 = "jnz ";
                } else {
                    ptr++;
                    return;
                }
                comm2 += operands2[1] + " " + operands2[2];
            }
            commands[ptr2] = comm2;
        }
        ptr++;
    }

    protected void jnz(String op1, String op2) {
        int val1 = getValue(op1),
            val2 = getValue(op2);
        if (val1 != 0) {
            ptr += val2;
        } else {
            ptr++;
        }
    }

    protected void dec(String op) {
        registers[op.charAt(0) - 'a']--;
        ptr++;
    }

    protected void inc(String op) {
        registers[op.charAt(0) - 'a']++;
        ptr++;
    }

    protected void cpy(String op1, String op2) {
        registers[op2.charAt(0) - 'a'] = getValue(op1);
        ptr++;
    }

    protected void out(String op) {
        int val = getValue(op);
        output.append(val);
        ptr++;
    }

}
