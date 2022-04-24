camelCase = input("camelCase: ")
snake_case = ""
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        snake_case = snake_case + "_" + camelCase[i].lower()
    else:
        snake_case = snake_case + camelCase[i]

print(f"snake_case: {snake_case}")
