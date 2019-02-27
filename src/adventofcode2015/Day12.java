
package adventofcode2015;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

import utils.Input;

/**
 * https://adventofcode.com/2015/day/12
 */
public class Day12 {

    static final String js =
            "function count(obj, excludeRed) {" +
            "    total = 0;" +
            "    for (prop in obj) {" +
            "        val = obj[prop];" +
            "        if (!Array.isArray(obj) && excludeRed && val == 'red') return 0;" +
            "        if (typeof val == 'number') total += val;" +
            "        else if (typeof val == 'object') total += count(val, excludeRed);" +
            "    }" +
            "    return total" +
            "}";

    public static void main(String[] args) throws Exception {
        String input = new Input(2015, 12).strings().get(0);
        ScriptEngine engine = new ScriptEngineManager().getEngineByName("JavaScript");
        engine.eval(js);
        engine.eval("input = " + input);
        System.err.println(((Double)engine.eval("count(input, false)")).intValue());
        System.err.println(((Double)engine.eval("count(input, true)")).intValue());
    }

}
