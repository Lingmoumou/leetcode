

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index=-1
        for i in range(len(nums)):
            print(nums)
            if nums[i]==0 and index==-1:
                index=i
            elif nums[i]!=0 and index!=-1:
                for j in range(index,i):
                    if nums[j]==0:
                        index=j
                        break
                temp=nums[i]
                nums[i]=nums[index]
                nums[index]=temp
            else:
                continue
        return nums


def main():
    s=Solution()
    result=s.moveZeroes([0,1,0,3,12,0])
    # print()
    # print("---")
    print(s.moveZeroes([1,2]))

if __name__ == '__main__':
    main()         

