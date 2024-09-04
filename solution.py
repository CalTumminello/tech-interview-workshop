class Solution:
    def rob(self, nums: List[int]) -> int:
        money = 0
        maxNum = max(nums)
        # Edge case where borders are greater than middle element
        if (len(nums) == 3) and (nums[0] + nums[len(nums)-1] > maxNum):
            money += nums[0] + nums[len(nums)-1]
            nums[0] = 0
            nums[1] = 0
            nums[len(nums)-2] = 0
            nums[len(nums)-1] = 0   
        # main loop
        while maxNum >= 0:
            # finds best house
            maxNum = max(nums)
            # robs house
            money += maxNum
            # ignores neighbors around robbed house (watching for list bounds)
            if nums.index(maxNum)-1 >= 0 :
                nums[nums.index(maxNum)-1] = 0
            if nums.index(maxNum)+1 < len(nums):
                nums[nums.index(maxNum)+1] = 0
            nums[nums.index(maxNum)] = 0     
            print(nums) 
            # exit condition
            if maxNum == 0:
                maxNum = -1 
        #moolah
        return money
