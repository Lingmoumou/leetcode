class Solution:
    def removeDuplicates(self, nums):
        """
        给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
        :type nums: List[int]
        :rtype: int
        """
        idx=0
        n=len(nums)-1
        for i in range(n):
            if nums[idx]==nums[idx+1]:
                nums.remove(nums[idx])
            else:
                idx=idx+1
        return nums        


def main():
    s=Solution()
    print(s.removeDuplicates([1,1,2])) # [1,2]
    print(s.removeDuplicates([1])) # [1]
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # [0,1,2,3,4]

if __name__ == '__main__':
    main()         
