# His hypothesis: naming the parameter `nums` makes it the same variable as the outer `nums`.

def stretch(nums):
    nums.append(0)
    nums = nums + [1, 1]
    nums.append(2)

nums = [7, 8]
stretch(nums)

print(nums)
print(len(nums))
print(nums[len(nums) - 1])

print("---")

# Same moment, same name, two different values.
def show(nums):
    nums = nums + [1, 1]
    print("inside the function: ", nums)

nums = [7, 8]
show(nums)
print("outside the function:", nums)
