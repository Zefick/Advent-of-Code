package adventofcode2016;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day22 {

    static int nodes[][][] = new int[36][30][3];

    // Size  Used  Available
    static Pattern p = Pattern.compile("/dev/grid/node-x(\\d+)-y(\\d+)\\s+(\\d+)T\\s+(\\d+)T\\s+(\\d+)T");

    public static void main(String[] args) {
        List<String> df = new Input(2016, "input22.txt").strings();
        for (String s : df) {
            Matcher m = p.matcher(s);
            m.find();
            int x = Integer.parseInt(m.group(1));
            int y = Integer.parseInt(m.group(2));
            nodes[x][y][0] = Integer.parseInt(m.group(3));
            nodes[x][y][1] = Integer.parseInt(m.group(4));
            nodes[x][y][2] = Integer.parseInt(m.group(5));
        }
        int n = 0;
        for (int i=0; i<36*30; i++) {
            if (nodes[i/30][i%30][1] == 0) continue;
            for (int j=0; j<36*30; j++) {
                if (i != j && nodes[i/30][i%30][1] <= nodes[j/30][j%30][2]) n++;
            }
        }
        for (int i=0; i<36; i++) {
            for (int j=0; j<30; j++) {
                System.err.printf(" [%3d / %3d] ", nodes[i][j][1], nodes[i][j][0]);
            }
            System.err.println();
        }
        System.out.println(n);


    }

}
