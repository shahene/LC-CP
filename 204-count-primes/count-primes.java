class Solution {
    public int countPrimes(int n) {
        /*
        Sieve of Eratosthenes
        every composite number has at least one prime factor
        for each prime factor starting from 2, ignore multiples of that prime factor as they will be composite
        use a boolean array
        where True represents a certain composite number
        and False represents a potential prime number
        [False, False, False, ...]
        starting at index 2, change the value at multiple index i in boolean array to True
        return number of False values in array

        n = 10
        [False, False, False, False, False, False, False, False, False, False]
        */
        boolean[] booleanArray = new boolean[n];
        int primeCount = 0;
        for (int i = 2; i < n; i++) {
            if (booleanArray[i]) continue;
            primeCount += 1;
            int primeStart = i + i;
            if (primeStart < n) {
                for (int k = primeStart; k < n; k += i) {
                    booleanArray[k] = true;
                }
            }
           

        }
        return primeCount;
    }
     
}