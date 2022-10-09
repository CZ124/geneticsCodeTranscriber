import java.util.HashMap;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
    }

}

    // Leetcode 70
    public static int recursionMethod(int n) {
        if (n == 1) // if only one stair left
        {
            return 1;
        }

        if (n == 2) // if only two stairs left
        {
            return 2;
        }

        return recursionMethod(n - 1) + recursionMethod(n - 2); // if staires > 3, return if first step is 1 and if
                                                                // first step is 2
    }

    public static int hashmapMethod(int n)
    {
        HashMap<Integer, Integer> climbStairs = new HashMap<Integer, Integer>();

        if (n == 1) //if only one stair left
        {
            return 1;
        }

        if (n == 2) //if only two stairs left
        {
            return 2;
        }

        if (n >= 3 && null != climbStairs.get(n))
        {
            return climbStairs.get(n);
        }

        else
        {
            climbStairs.put(n, hashmapMethod(n-1) + hashmapMethod(n-2));
            //return hashmapMethod(n-1) + hashmapMethod(n-2);
        }
    }
