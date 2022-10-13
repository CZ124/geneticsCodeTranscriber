public class LeetCode509 {
    public static void main(String[] args) {
        
    }
    
    public static int loopMethod(int n) {
        
        if(n == 0)
        {
            return 0;
        }
        
        if(n == 1)
        {
            return 1;
        }
        
        int res = 0;
        int prev = 1;
        int prevPrev = 0;
        
        for (int i = 2; i <= n; ++i)
        {
            res = prev+prevPrev;
            
            prevPrev = prev;
            prev = res;
            
        }
        return res;

    }
}
