public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
    }

}

    // Leetcode 70
    public static int LC70(int n){
        if (n == 1) //if only one stair left
        {
            return 1;
        }

        if (n == 2) //if only two stairs left
        {
            return 2;
        }

        return LC70(n-1) + LC70(n-2); //if staires > 3, return if first step is 1 and if first step is 2
    }
