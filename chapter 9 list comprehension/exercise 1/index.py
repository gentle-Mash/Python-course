def reverse(l):
    reverse_list = []
    for item in l:
        reverse_list.append(item[::-1])
    return reverse_list

list1 = ["deku", "ochako", "lida"]
print(reverse(list1))

# by list comprehension

def reverse2(l):
    rev_list = [item[::-1] for item in l]
    return rev_list
print(reverse2(list1))
