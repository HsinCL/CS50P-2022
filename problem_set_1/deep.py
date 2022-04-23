ans = input("What is the Answer to the Great Question of Life, the Universe, and Everthing?")
valid_answer = ['42', 'forty-two', 'forty two']
ans_str = str(ans).lower()
if ans_str in valid_answer:
    print('Yes')
else:
    print('No')
