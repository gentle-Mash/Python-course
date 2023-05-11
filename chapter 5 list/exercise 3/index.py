words = ["abc", "xyz", "123"]

# def reverse_words(l):
#     rev_words = []
#     for i in range(len(l)):
#         popped = l.pop()
#         rev_words.insert(0, popped[::-1])
#     return rev_words

# print(reverse_words(words))

def reverse_small(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

print(reverse_small(words))