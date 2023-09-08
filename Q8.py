vowels =['a','e','i','o','u','A','E','I','O','U']
str = input("Input your string: ")
h = ''
for i in str:
    if i not in vowels:
     h += i
    else:
        continue
words = h.split()
ans = max(words, key = len)
print("Longest common subsequence: ", ans)