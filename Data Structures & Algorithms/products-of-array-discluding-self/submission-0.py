class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zc = 0
        d = [0]
        for i in nums:
            if i != 0:
                p *= i
            else:
                zc += 1
        if zc > 1 and len(nums)>1:
            return d * len(nums)
        output = []
        for j in nums:
            if zc:
                if j != 0:
                    output.append(0)
                else:
                    output.append(p)
            else:
                output.append(p//j)
        return output
        