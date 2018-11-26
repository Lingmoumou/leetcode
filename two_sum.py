
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(target==(nums[i]+nums[j])):
                    return [i,j]
    
    def twoSumByTwoPassHashTable(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp={}
        for i in range(len(nums)):
            temp[nums[i]]=i

        for j in range(len(nums)):
            complement=target-nums[j]
            if(temp.__contains__(complement) and temp.get(complement)!=j):
                return [temp.get(complement),j]
        
    def twoSumByOnePassHashTable(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp={}

        for j in range(len(nums)):
            complement=target-nums[j]
            if(temp.__contains__(complement)):
                return [temp.get(complement),j]
            temp[nums[j]]=j

def main():
    s=Solution()
    print(s.twoSum([2,7,11,15,17],32))
    print(s.twoSumByTwoPassHashTable([3,2,4],6))
    print(s.twoSumByOnePassHashTable([2,7,11,15,17],32))

if __name__ == '__main__':
    main()         



                    
                
            