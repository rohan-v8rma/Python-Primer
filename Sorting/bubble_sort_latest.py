list_1 = [76,85,34,23,65,12,9]
l = len(list_1)
for passes in range(0,l-1):
    for comparison in range(0,l-passes-1):
        if list_1[comparison] > list_1[comparison + 1]:
            list_1[comparison], list_1[comparison + 1] =list_1[comparison + 1], list_1[comparison]
        else:
            continue
print(list_1)        