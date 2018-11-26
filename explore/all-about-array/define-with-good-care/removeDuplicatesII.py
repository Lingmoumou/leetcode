class Solution:
    def removeDuplicates(self, nums):
        """
        给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
        :type nums: List[int]
        :rtype: int
        """
        idx=0
        while idx+2<len(nums):
            if nums[idx]==nums[idx+2]:
                nums.remove(nums[idx])
            elif nums[idx]!=nums[idx+2] and nums[idx]==nums[idx+1]:
                idx=idx+2
            elif nums[idx]!=nums[idx+2] and nums[idx]!=nums[idx+1]:
                idx=idx+1
        return len(nums)        


def main():
    s=Solution()
    print(s.removeDuplicates([1,1,1,2,2,3])) # [1,1,2,2,3]
    print(s.removeDuplicates([1])) # [1]
    print(s.removeDuplicates([1,1])) # [1]
    print(s.removeDuplicates([1,2])) # [1,2]
    print(s.removeDuplicates( [0,0,1,1,1,1,2,3,3])) # [0,0,1,1,2,3,3]

if __name__ == '__main__':
    main()         
