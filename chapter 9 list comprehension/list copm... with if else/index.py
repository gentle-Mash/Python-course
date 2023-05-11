list1 = [1,2,3,4,5,6,7,8,9]
nums = []
for i in list1:
    if i%2 == 0:
        nums.append(i*2)
    else:
        nums.append(-i)
print(nums)

nums2 = [i*2 if (i%2 == 0) else -i for i in list1]
print(nums2)