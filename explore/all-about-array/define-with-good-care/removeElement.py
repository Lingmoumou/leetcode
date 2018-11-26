import math

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # idx=-1
        # if nums.__contains__(val):
        #     for i in range(len(nums)):
        #         if nums[i]==val and idx==-1:
        #             idx=i
        #         elif nums[i]!=val and idx!=-1:
        #             temp=nums[i]
        #             nums[i]=nums[idx]
        #             nums[idx]=temp
        #             for j in range(idx,i+1):
        #                 if nums[j]==val:
        #                     idx=j
        #                     break
        #         else: # nums[i]!=val and idx==-1
        #             continue 
        #     return idx              
        # else:
        #     return len(nums)

        while val in nums:
            nums.remove(val)
        return len(nums)


        #  n = len(nums)
        # i = -1
        # # 定义nums[0...i]为非val的数列
        # j = 0
        # while j <= n-1:
        #     if nums[j] != val:
        #         i += 1
        #         nums[i] = nums[j]
        #     j += 1
        # return i+1
def main():
    s=Solution()

    print(s.removeElement([1],1)) #[]
    print(s.removeElement([2],3))  #[2]
    print(s.removeElement([4,5],4)) #[5]
    print(s.removeElement([4,5],5)) #[4]
    print(s.removeElement([3,2,2,3],3)) #[2,2]
    print(s.removeElement([0,1,2,2,3,0,4,2],2)) #[0,1,3,0,4]

if __name__ == '__main__':
    main()         

