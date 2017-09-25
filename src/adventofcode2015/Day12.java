
package adventofcode2015;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

import utils.Input;

public class Day12 {

    static final String js =
            "function count(obj) {" +
            "    total = 0;" +
            "    for (prop in obj) {" +
            "        val = obj[prop];" +
            "        if (!Array.isArray(obj) && val == 'red') return 0;" +
            "        if (typeof val == 'number') total += val;" +
            "        else if (typeof val == 'object') total += count(val);" +
            "    }" +
            "    return total" +
            "}";

    public static void main(String[] args) throws Exception {
        String input = new Input(2015, "input12.txt").strings().get(0);
        ScriptEngine engine = new ScriptEngineManager().getEngineByName("JavaScript");
        engine.eval(js);
        engine.eval("print(count(" + input + "))");
    }

}
