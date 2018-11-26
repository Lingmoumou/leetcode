class Solution:
    def sortColors(self, nums):
        """
        给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
        此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j=len(nums)-1
        i=0
        while i<j:
            if nums[i]>nums[len(nums)-1]:
                temp=nums[i]
                nums[i]=nums[len(nums)-1]
                nums[len(nums)-1]=temp
                i=i+1
            elif nums[i]==nums[len(nums)-1]:
                # if i>0:
                if nums[i]==nums[j]:
                    j=j-1
                if nums[i]>nums[j] and i<len(nums)-i:
                    # j=len(nums)-i
                        temp=nums[i]
                        nums[i]=nums[j]
                        nums[j]=temp
                        i=i+1
                elif nums[i]>nums[i+1]:
                    temp=nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1]=temp 
                    i=i+1

            elif nums[i]<nums[len(nums)-1] :
                # j=len(nums)-i-1
                if i==0:
                    j=j-1
                if nums[i]>nums[j] and i<j:
                # j=len(nums)-i
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                elif nums[i]>nums[i+1]:
                    temp=nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1]=temp   
                elif nums[0:i].__contains__(0):
                    temp=nums[i]
                    nums[i]=nums[nums[0:1].index(0)]
                    nums[nums[0:1].index(0)]=temp
                i=i+1  
            else:
                continue
        return nums

def main():
    s=Solution()
    print(s.sortColors([1,1,2])) # [1,1,2]
    print(s.sortColors([1,0,2])) # [0,1,2]
    print(s.sortColors([1])) # [1]
    print(s.sortColors([2,1])) # [1]
    print(s.sortColors([2,0,2,1,1,0])) # [0,0,1,1,2,2]
    print(s.sortColors([0,1,0,1,0,2])) # [0,0,0,1,1,2]
    print(s.sortColors([1,1,0,2,0,1])) # [0,0,1,1,1,2]
    print(s.sortColors([2,1,0,2,1,2])) # [0,0,1,1,1,2]

if __name__ == '__main__':
    main()         
