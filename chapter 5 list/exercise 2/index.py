numbers = list(range(1,6))

def reverse(l):
    revers_list = []
    for i in range(len(l)):
        popped = l.pop()
        revers_list.append(popped)
    return revers_list

print(reverse(numbers))