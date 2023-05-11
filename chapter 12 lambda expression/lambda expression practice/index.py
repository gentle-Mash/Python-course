def even_odd(a):
    return a%2 == 0
print(even_odd(5))

even_odd2 = lambda a : a%2 == 0
print(even_odd2(2))

last_char = lambda a: a[-1]
print(last_char("deku"))

big = lambda a: True if a > 5 else False
big2 = lambda a: a>5

print(big(6))
print(big2(6))