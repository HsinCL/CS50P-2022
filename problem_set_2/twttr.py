twttr = input("Input: ")
vowel = ['a', 'e', 'i', 'o', 'u']
output = ""
for i in range(len(twttr)):
    if twttr[i] in vowel: 
        continue
    else:
        output = output + twttr[i]
print("output:", output)
