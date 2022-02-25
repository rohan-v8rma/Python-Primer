
import json
sentence = """hello my name is rohan. hello world """
words = sentence.split()
word_count = {}
""" First method """
for i in words:
    count = 0
    for t in words:
        if t == i:
            count += 1
        else:
            continue
    word_count[i] = count            
print(json.dumps(word_count, indent = 2))    

"""Second method"""
word_count2 = {}
for word in words:
    word_count2[word] = word_count2.get(word,0) + 1 
"""what this statement does is that if the word hasn't been registered in the count even once,
it returns the second argument which indicates that the key isnt present in dictionary. In this case,
the second argument is 0 which causes count of the word to be 0 """
print(json.dumps(word_count2, indent = 2))
