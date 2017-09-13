package adventofcode2016;

import java.util.Collections;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

import utils.Input;

/**
 * The most tedious task. Let's fun with some OOP.
 */
public class Day21 {

    static Pattern p[] = {
            Pattern.compile("swap position (\\d+) with position (\\d+)"),
            Pattern.compile("swap letter (.) with letter (.)"),
            Pattern.compile("rotate (\\w+) (\\d+)"),
            Pattern.compile("rotate based on position of letter (.)"),
            Pattern.compile("reverse positions (\\d+) through (\\d+)"),
            Pattern.compile("move position (\\d+) to position (\\d+)")
    };

    interface Action {
        char[] encript(char[] s);
        default char[] decript(char[] s) {
            // by default decript and encript do the same work.
            // It is true for half of the operations.
            return encript(s);
        }
    }

    static class Swap1 implements Action {
        int a, b;
        Swap1(int a, int b) {
            this.a = a;
            this.b = b;
        }
        @Override
        public char[] encript(char s[]) {
            s = s.clone();
            char t = s[a];
            s[a] = s[b];
            s[b] = t;
            return s;
        }
    }

    static class Swap2 implements Action {
        char a, b;
        Swap2(char a, char b) {
            this.a = a;
            this.b = b;
        }
        @Override
        public char[] encript(char s[]) {
            int i = getIndex(s, a);
            int j = getIndex(s, b);
            s = s.clone();
            char t = s[i];
            s[i] = s[j];
            s[j] = t;
            return s;
        }
    }

    static class Rotate1 implements Action {
        int n;
        public Rotate1(int n) {
            this.n = n;
        }
        static char[] rotate(char s[], int n) {
            if (n < 0) {
                n += s.length;
            }
            return Day21.rotate(s, n);
        }
        @Override
        public char[] encript(char[] s) {
            return rotate(s, n);
        }
        @Override
        public char[] decript(char[] s) {
            return rotate(s, -n);
        }
    }

    static char[] rotate(char[] s, int n) {
        char s2[] = new char[s.length];
        for (int j=0; j<s.length; j++) {
            s2[j] = s[(s.length*2+j-n) % s.length];
        }
        return s2;
    }

    static class Rotate2 implements Action {
        char c;
        static char d[] = {7, 7, 2, 6, 1, 5, 0, 4};
        public Rotate2(char c) {
            this.c = c;
        }
        @Override
        public char[] encript(char[] s) {
            int n = getIndex(s, c) + 1;
            if (n > 4) n++;
            return Day21.rotate(s, n);
        }
        @Override
        public char[] decript(char[] s) {
            int n = d[getIndex(s, c)];
            return Day21.rotate(s, n);
        }
    }

    static class Reverse implements Action {
        int a, b;
        public Reverse(int a, int b) {
            this.a = a;
            this.b = b;
        }
        @Override
        public char[] encript(char[] s) {
            char s2[] = s.clone();
            for (int j=0; j<=b-a; j++) {
                s2[a+j] = s[b-j];
            }
            return s2;
        }
    }

    static class Move implements Action {
        int a, b;
        public Move(int a, int b) {
            this.a = a;
            this.b = b;
        }
        static char[] move(char s[], int a, int b) {
            char s2[] = s.clone();
            if (b > a) {
                for (int j=a; j<b; j++) {
                    s2[j] = s[j+1];
                }
                s2[b] = s[a];
            } else {
                s2[b] = s[a];
                for (int j=b+1; j<=a; j++) {
                    s2[j] = s[j-1];
                }
            }
            return s2;
        }
        @Override
        public char[] encript(char[] s) {
            return move(s, a, b);
        }
        @Override
        public char[] decript(char[] s) {
            return move(s, b, a);
        }
    }

    static Action createAction(String text) {
        for (int i=0; i<6; i++) {
            Matcher m = p[i].matcher(text);
            if (m.find()) {
                if (i == 0) {
                    return new Swap1(Integer.parseInt(m.group(1)), Integer.parseInt(m.group(2)));
                } else if (i == 1) {
                    return new Swap2(m.group(1).charAt(0), m.group(2).charAt(0));
                } else if (i == 2) {
                    int n = Integer.parseInt(m.group(2));
                    return new Rotate1(m.group(1).equals("left") ? -n : n);
                } else if (i == 3) {
                    return new Rotate2(m.group(1).charAt(0));
                } else if (i == 4) {
                    return new Reverse(Integer.parseInt(m.group(1)), Integer.parseInt(m.group(2)));
                } else if (i == 5) {
                    return new Move(Integer.parseInt(m.group(1)), Integer.parseInt(m.group(2)));
                }
            }
        }
        return null;
    }

    static int getIndex(char str[], char c) {
        for (int i=0; ; i++) {
            if (str[i] == c) return i;
        }
    }

    public static void main(String[] args) {
        char input[] = "fbgdceah".toCharArray();

        List<Action> commands = new Input(2016, "input21.txt").strings().stream()
                .map(Day21::createAction)
                .collect(Collectors.toList());
        Collections.reverse(commands);

        for (Action action : commands) {
            input = action.decript(input);
        }
        System.out.println(new String(input));
    }

}
