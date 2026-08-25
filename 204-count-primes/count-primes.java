class Solution {
    public int countPrimes(int n) {
        if (n <= 2) return 0;
        boolean[] isPrime = new boolean[n];

        // false = potentially prime
        // true = composite

        int primeCount = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) {
                continue;
            }
            primeCount++;
            if ((long) i * i < n) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = true;
                }
            }
        }
        return primeCount;
    }
    
}