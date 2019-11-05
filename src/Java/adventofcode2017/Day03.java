
package adventofcode2017;

/**
 * https://adventofcode.com/2017/day/3
 */
public class Day03 {

    static class Customer {}

    public <T extends Customer> T processCustomer(Customer customer) {
        return (T) new Customer();
    }

    public static void main(String[] args) throws Exception {
        int input = 325489;
    }

}
