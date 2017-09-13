
package adventofcode2016;

import java.awt.Point;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.IntConsumer;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * Class for finding paths between
 * @param <T>
 */
public class PathFinder<T> {

    protected Function<T, Stream<T>> stepFunction;

    protected Runnable finishCallback;

    protected IntConsumer stepCallback;

    protected Consumer<T> visitCallback;

    protected int steps;

    protected volatile boolean stop;

    protected Set<T> visited;

    public void setStepFunction(Function<T, Stream<T>> stepFunction) {
        this.stepFunction = stepFunction;
    }

    public void setFinishCallback(Runnable finishCallback) {
        this.finishCallback = finishCallback;
    }

    public void setStepCallback(IntConsumer stepCallback) {
        this.stepCallback = stepCallback;
    }

    public void setVisitCallback(Consumer<T> visitCallback) {
        this.visitCallback = visitCallback;
    }

    public void stop() {
        stop = true;
    }

    public int getSteps() {
        return steps;
    }

    public Set<T> getVisited() {
        return visited;
    }

    public void run(T start, T dest) {
        visited = new HashSet<>();
        List<T> current = Collections.singletonList(start);
        steps = 0;
        stop = false;
        while (!current.isEmpty() && !stop) {
            steps++;
            current = current.stream()
                .flatMap(stepFunction).distinct()
                .filter(p -> !visited.contains(p))
                .collect(Collectors.toList());
            if (visitCallback != null) {
                current.forEach(visitCallback);
            }
            if (dest != null && finishCallback != null
                    && current.contains(dest)) {
                finishCallback.run();
            }
            visited.addAll(current);
            if (stepCallback != null) {
                stepCallback.accept(steps);
            }
        }
    }

    /**
     * PathFinder for 2D Points with integer coordinates.
     */
    public static class PathFinder2D extends PathFinder<Point> {

        private static int DIRECTIONS[][] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        private Predicate<Point> movePredicate;

        public void setMovePredicate(Predicate<Point> movePredicate) {
            this.movePredicate = movePredicate;
        }

        public PathFinder2D() {
            super.stepFunction = p -> Stream.of(DIRECTIONS)
                    .map(d -> new Point(p.x+d[1], p.y+d[0]))
                    .filter(d -> movePredicate.test(d));
        }

    }

}
