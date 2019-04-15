#暴力穷举
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for key,values in enumerate(nums):
            temp = target - values
            for key2,values2 in enumerate(nums[key+1:]):
                if temp == values2:
                    return [key,key+key2+1]

#先快排，获取下标关键字，从头尾开始遍历
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_list = sorted(range(len(nums)),key=lambda k:nums[k])
        head = 0
        tail = len(nums) - 1
        sum_result = nums[sort_list[head]] + nums[sort_list[tail]]
        while sum_result != target:
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head += 1
            sum_result = nums[sort_list[head]] + nums[sort_list[tail]]
        return [sort_list[head],sort_list[tail]]
                


            
            
            
        