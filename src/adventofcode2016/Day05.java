
package adventofcode2016;

import utils.MD5;

public class Day05 {

    public static void main(String[] args) {
        int index = 0;
        String id = "wtnhxymk";
        char pass[] = new char[8];

        for (int i=0; i<8;) {
            String md5 = MD5.encode(id + index);
            if (md5.startsWith("00000")) {
                pass[i] = md5.charAt(5);
                i++;
            }
            index++;
        }
        System.out.println(new String(pass));

        pass = new char[8];
        index = 0;
        for (int i=0; i<8;) {
            String md5 = MD5.encode(id + index);
            if (md5.startsWith("00000")) {
                int p = md5.charAt(5) - '0';
                if (p>=0 && p<8 && pass[p] == 0) {
                    pass[p] = md5.charAt(6);
                    i++;
                }
            }
            index++;
        }
        System.out.println(new String(pass));
    }

}

