package adventofcode2016;

import java.util.Arrays;

/**
 * https://adventofcode.com/2016/day/18
 */
public class Day18 {

    static String start =
            "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.";

    public static void main(String[] args) {
        int len = start.length();
        int map1[] = start.chars().toArray();
        int cnt = 0;
        for (int i=0; i<400000; i++) {
            if (i == 40) {
                System.err.println(cnt);
            }
            cnt += Arrays.stream(map1).filter(x -> x == '.').count();
            int map2[] = new int[len];
            for (int j=0; j<len; j++) {
                boolean a = (j==0) || (map1[j-1]=='.'),
                        b = map1[j]=='.',
                        c = (j==len-1) || (map1[j+1]=='.'),
                        d = (a!=b && a!=c) || (c!=a && c!=b);
                map2[j] = d ? '^' : '.';
            }
            map1 = map2;
        }
        System.err.println(cnt);
    }

}
