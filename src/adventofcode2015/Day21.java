package adventofcode2015;

public class Day21 {

    static boolean simulate(int damage, int armor) {
        for (int hp1 = 100, hp2 = 100;;) {
            if ((hp1 = hp1-Math.max(1, damage - 2)) <= 0) return true;
            if ((hp2 = hp2-Math.max(1, 8 - armor)) <= 0) return false;
        }
    }

    public static void main(String[] args) {
        int weapon[][] = {{8, 4}, {10, 5}, {25, 6}, {40, 7}, {74, 8}};
        int armor[][] = {{0, 0}, {13, 1}, {31, 2}, {53, 3}, {75, 4}, {102, 5}};
        int ring[][] = {{0, 0, 0}, {0, 0, 0}, {25, 1, 0}, {50, 2, 0}, {100, 3, 0}, {20, 0, 1}, {40, 0, 2}, {80, 0, 3}};

        int best = 0;
        for (int[] w : weapon) {
            for (int a[] : armor) {
                for (int r1[] : ring) {
                    for (int r2[] : ring) {
                        if (r1 == r2) continue;
                        int gold = w[0] + a[0] + r1[0] + r2[0];
                        if (gold > best) {
                            if (!simulate(w[1] + r1[1] + r2[1], a[1] + r1[2] + r2[2])) {
                                best = gold;
                            }
                        }
                    }
                }
            }
        }
        System.out.println(best);
    }

}
