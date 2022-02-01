def even(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
even_till_20 = list(even(21))
print(even_till_20)
