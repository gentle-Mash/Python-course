def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter("Ochako Uraraka"))