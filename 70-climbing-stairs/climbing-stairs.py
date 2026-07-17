class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        input: integer n (takes n steps to reach the top)
        output: ways to climb to the top
            0, 1, 2, 3, 4, 5
        DP  [8 5  3  2  1 1]
        '''
        one, two = 1, 1
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one

        