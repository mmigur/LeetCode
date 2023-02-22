def twoSum(nums, target):
        temp_index = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                        temp_index.append(i)
                        temp_index.append(j)

        return temp_index

print("Hello, word!")