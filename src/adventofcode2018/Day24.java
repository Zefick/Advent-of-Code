package adventofcode2018;

import java.util.*;
import java.util.regex.*;

import utils.Input;

/**
 * https://adventofcode.com/2018/day/24
 */
public class Day24 {

    static class Group {
        boolean faction;
        int units, hp, initiative, power;
        String weak, immune, attack;
        Group(boolean f, int u, int hp, int init, String immune,
                    String weak, String atk, int pwr) {
            this.faction = f;
            this.units = u;
            this.hp = hp;
            this.initiative = init;
            this.immune = immune;
            this.weak = weak;
            this.attack = atk;
            this.power = pwr;
        }
    }

    static List<Group> fillGroups() {
        List<String> input = new Input(2018, 24).strings();
        Pattern p = Pattern.compile("(\\d+) units each with (\\d+) hit points " // 1, 2
                + "(\\((\\w+) to ([a-z, ]+)(; (\\w+) to ([a-z, ]+))?\\) )?"  // (3 (4 5) (6 (7 8))))
                + "with an attack that does (\\d+) (\\w+) damage at initiative (\\d+)");  // 9, 10, 11
        List<Group> groups = new ArrayList<>();
        boolean faction = true;
        for (String s : input) {
            if (s.equals("Infection:")) faction = false;
            Matcher m = p.matcher(s);
            if (m.find()) {
                int units = Integer.parseInt(m.group(1));
                int hp = Integer.parseInt(m.group(2));
                String immune = "", weak = "", atk = m.group(10);
                int power = Integer.parseInt(m.group(9));
                int init = Integer.parseInt(m.group(11));
                for (int g = 4; g <= 7; g += 3) {
                    if (m.group(g) != null) {
                        if (m.group(g).equals("immune")) {
                            immune = m.group(g + 1);
                        } else {
                            weak = m.group(g + 1);
                        }
                    }
                }
                groups.add(new Group(faction, units, hp, init, immune, weak, atk, power));
            }
        }
        return groups;
    }

    public static void main(String[] args) throws Exception {
        List<String> results = new ArrayList<>();
        all:
        for (int v = 0; v<1000; v++) {
            int boost = v;
            List<Group> groups = fillGroups();
            groups.stream().filter(g -> g.faction).forEach(g -> g.power += boost);
            for (int t=0; t<10000; t++) {
                Map<Group, Group> targets = new HashMap<>();
                // select targets
                groups.stream().sorted(Comparator
                            .<Group, Integer>comparing(g -> -g.units * g.power)
                            .thenComparing(g -> -g.initiative))
                        .forEach(g -> groups.stream()
                                .filter(g2 -> !targets.containsValue(g2)
                                        && g2.units > 0
                                        && g.faction == !g2.faction
                                        && !g2.immune.contains(g.attack))
                                .max(Comparator.<Group, Integer>comparing(g2 -> 
                                            (g2.weak.contains(g.attack) ? (g.units * g.power * 2) : (g.units * g.power)))
                                        .thenComparing(g2 -> g2.units * g2.power)
                                        .thenComparing(g2 -> g2.initiative))
                                .ifPresent(g2 -> targets.put(g, g2))
                        );
                // attack
                groups.stream()
                        .filter(g -> targets.containsKey(g))
                        .sorted(Comparator.comparing(g -> -g.initiative))
                        .forEach(g -> {
                            if (g.units <= 0) return;
                            Group g2 = targets.get(g);
                            int damage = g2.weak.contains(g.attack)
                                    ? (g.units * g.power * 2)
                                    : (g.units * g.power);
                            g2.units -= damage / g2.hp;
                        });

                groups.removeIf(g -> g.units <= 0);
                if (groups.stream().allMatch(g -> g.faction) || groups.stream().allMatch(g -> !g.faction)) {
                    boolean faction = groups.get(0).faction;
                    results.add(String.format(
                            "boost %d: time %d, %b, %d",
                            boost, t, faction, groups.stream().mapToInt(g -> g.units).sum()));
                    if (faction) break all;
                    break;
                }
            }
        }
        System.err.println(results.get(0));
        System.err.println(results.get(results.size()-1));
    }
}
