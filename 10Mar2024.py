from ast import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1 = set()
        for num in nums1 :
            st1.add(num)
        st2 = set()
        for num in nums2 :
            st2.add(num)
        ans = [];
        for val in st1 :
            if val in st2 :
                ans.append(val)
        return ans