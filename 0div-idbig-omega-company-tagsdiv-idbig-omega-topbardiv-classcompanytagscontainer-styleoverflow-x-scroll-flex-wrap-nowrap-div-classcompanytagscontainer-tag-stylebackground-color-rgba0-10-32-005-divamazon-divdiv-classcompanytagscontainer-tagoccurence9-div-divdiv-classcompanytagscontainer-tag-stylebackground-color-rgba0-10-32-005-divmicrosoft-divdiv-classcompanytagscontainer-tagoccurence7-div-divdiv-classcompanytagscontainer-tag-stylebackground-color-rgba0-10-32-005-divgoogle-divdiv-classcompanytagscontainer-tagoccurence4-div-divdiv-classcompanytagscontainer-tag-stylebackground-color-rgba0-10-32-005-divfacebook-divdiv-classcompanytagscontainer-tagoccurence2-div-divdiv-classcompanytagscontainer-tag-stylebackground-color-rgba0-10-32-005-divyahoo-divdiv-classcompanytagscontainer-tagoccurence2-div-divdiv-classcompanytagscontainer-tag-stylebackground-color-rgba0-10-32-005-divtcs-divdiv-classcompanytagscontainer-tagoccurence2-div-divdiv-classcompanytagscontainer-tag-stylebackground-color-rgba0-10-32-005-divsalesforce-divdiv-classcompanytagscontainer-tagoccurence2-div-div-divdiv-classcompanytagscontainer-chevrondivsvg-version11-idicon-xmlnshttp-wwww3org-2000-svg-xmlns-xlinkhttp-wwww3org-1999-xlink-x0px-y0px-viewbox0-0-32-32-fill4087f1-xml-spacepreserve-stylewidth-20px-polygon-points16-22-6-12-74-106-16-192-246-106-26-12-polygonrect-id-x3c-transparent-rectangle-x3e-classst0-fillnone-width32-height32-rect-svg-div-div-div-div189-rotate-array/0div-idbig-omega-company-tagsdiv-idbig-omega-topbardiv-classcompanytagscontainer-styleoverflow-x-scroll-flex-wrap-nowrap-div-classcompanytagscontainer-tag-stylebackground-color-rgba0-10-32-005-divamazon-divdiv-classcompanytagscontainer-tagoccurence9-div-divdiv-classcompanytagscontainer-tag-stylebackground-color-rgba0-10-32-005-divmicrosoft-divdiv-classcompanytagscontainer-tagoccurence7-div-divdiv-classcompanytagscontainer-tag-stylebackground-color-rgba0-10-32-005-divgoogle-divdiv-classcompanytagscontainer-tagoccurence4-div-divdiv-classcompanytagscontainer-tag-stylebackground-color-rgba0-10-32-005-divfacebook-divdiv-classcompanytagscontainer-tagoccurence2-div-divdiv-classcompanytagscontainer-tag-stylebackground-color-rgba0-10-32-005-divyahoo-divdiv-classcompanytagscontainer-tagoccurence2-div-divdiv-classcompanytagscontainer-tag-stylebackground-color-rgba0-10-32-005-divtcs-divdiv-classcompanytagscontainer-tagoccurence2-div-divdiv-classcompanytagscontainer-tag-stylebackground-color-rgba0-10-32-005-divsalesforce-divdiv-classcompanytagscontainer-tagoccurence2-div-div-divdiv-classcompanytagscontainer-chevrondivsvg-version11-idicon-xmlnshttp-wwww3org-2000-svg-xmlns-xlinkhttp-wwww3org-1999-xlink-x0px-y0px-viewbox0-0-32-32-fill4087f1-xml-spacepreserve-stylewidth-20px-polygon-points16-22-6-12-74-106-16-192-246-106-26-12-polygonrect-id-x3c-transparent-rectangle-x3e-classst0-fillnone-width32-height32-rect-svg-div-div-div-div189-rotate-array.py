class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle the case where k is larger than the length of nums

        def reverse_list(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse_list(0, n - 1)  # Reverse the entire list
        reverse_list(0, k - 1)  # Reverse the first k elements
        reverse_list(k, n - 1)  # Reverse the remaining elements
        
        