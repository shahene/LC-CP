class Solution {
    public int maxProduct(int[] nums) {
        int f_biggest = (int) Float.NEGATIVE_INFINITY;
        int s_biggest = (int) Float.NEGATIVE_INFINITY;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > f_biggest) {
                int tmp = f_biggest;
                f_biggest = nums[i];
                s_biggest = tmp;
            } else if (nums[i] > s_biggest) {
                s_biggest = nums[i];
            }
        }
        return (f_biggest - 1) * (s_biggest - 1);
    }
}