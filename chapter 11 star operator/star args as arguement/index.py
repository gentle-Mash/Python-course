def multiply(*args):
    multi = 1
    for i in args:
        multi *= i
    return multi
nums=[1,2,3,4]
nums2=(1,2,3,4)

print(multiply(nums))
print(multiply(nums2))
# so here it's hust printing my original list and tuple but my multiply isn't working
#you can fix this by previous methods like indexing and removing the * symbole
# but you can simply use *args as aguement like

print(multiply(*nums))
print(multiply(*nums2))
#by doing this your list and tuple will be unpacked