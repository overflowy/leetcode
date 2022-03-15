from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.findMedian(self.mergeSortedArrays(nums1, nums2))

    def mergeSortedArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        merged: List[int] = []

        i = 0
        limit = len(nums1)

        while i < limit:
            if not nums2:
                merged += nums1[i:]
                break
            if nums1[i] < nums2[0]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2.pop(0))

        merged += nums2
        return merged

        # return sorted(nums1 + nums2)  # naive

    def findMedian(self, nums: List[int]):
        if len(nums) % 2 != 0:
            return nums[len(nums) // 2]

        left = nums[len(nums) // 2 - 1]
        right = nums[len(nums) // 2]

        return (left + right) / 2.0
