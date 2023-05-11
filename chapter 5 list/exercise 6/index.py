mixed = [1,2,3,[3,4,9],"a","b","c",["d","e","f"]]

def count_list(l):
    counted = 0
    for i in l:
        if type(i) == type(l):
            counted += 1
    return counted

print(count_list(mixed))
