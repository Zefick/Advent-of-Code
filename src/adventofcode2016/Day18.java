package adventofcode2016;

import java.util.Arrays;

public class Day18 {

    static String start =
            "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^";

    static int countSafe(int m[]) {
        return (int)Arrays.stream(m).filter(x -> x == '.').count();
    }

    public static void main(String[] args) {
        int lines = 400000;
        int len = start.length();
        int map1[] = start.chars().toArray();

        int cnt = 0;
        for (int i=0; i<lines-1; i++) {
            cnt += countSafe(map1);
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

        System.out.println(cnt + countSafe(map1));
    }

}
