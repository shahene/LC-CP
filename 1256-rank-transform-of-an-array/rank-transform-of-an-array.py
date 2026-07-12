class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # sort the array, keep dict for easy access, second pass append "rank" to res
        arr_map = collections.defaultdict(int)
        arr_sorted = sorted(arr)
        index = 1
        res= []
        for n in arr_sorted:
            if arr_map[n] == 0:
                arr_map[n] = index
                index += 1
        for i in range(len(arr)):
            res.append(arr_map[arr[i]])

        return res

