num1 = [1,2,3,4,5]
num2 = [4,5,6,7,8]

def common_nums(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output


print(common_nums(num1,num2))