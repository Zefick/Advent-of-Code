
package adventofcode2017;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.Input;

public class Day07 {

    static class Node {
        String name;
        String[] children;
        int weigth;
        Node parent;
    }

    static Map<String, Node> tower = new HashMap<>();

    private static int checkWeigth(Node node) {
        if (node.children.length > 0) {
            int weigths[] = Arrays.stream(node.children)
                    .mapToInt(name -> checkWeigth(tower.get(name))).toArray();

            if (Arrays.stream(weigths).distinct().count() > 1) {
                System.out.println(Arrays.toString(weigths));
                System.out.println(Arrays.toString(
                        Arrays.stream(node.children)
                            .mapToInt(name -> tower.get(name).weigth).toArray()));
                System.out.println();
            }
            return node.weigth + Arrays.stream(weigths).sum();
        }
        return node.weigth;
    }

    public static void main(String[] args) throws Exception {
        List<String> input = new Input(2017, "input07.txt").strings();

        Pattern p = Pattern.compile("([a-z]+) \\((\\d+)\\)( -> (([a-z]+(\\,\\s)?)*))?");

        for (String s : input) {
            Matcher m = p.matcher(s);
            m.find();
            Node node = new Node();
            node.name = m.group(1);
            node.weigth = Integer.parseInt(m.group(2));
            node.children = Optional.ofNullable(m.group(4))
                    .map(children -> children.split(",\\s+"))
                    .orElse(new String[0]);
            tower.put(node.name, node);
        }

        for (Node node : tower.values()) {
            for (String child : node.children) {
                tower.get(child).parent = node;
            }
        }
        Node root = tower.values().stream()
                .filter(node -> node.parent == null)
                .findFirst().get();

        System.out.println(root.name);

        checkWeigth(root);
    }

}
