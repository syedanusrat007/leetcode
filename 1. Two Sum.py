 def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for key,value in enumerate(nums):
            if target - value in dic:
                return [dic[target - value],key]
            else:
                dic[value] = key
