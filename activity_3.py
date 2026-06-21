ages = [19,20,13,47]
for age in ages:
    if age < 18:
        print(age,"not allowed")
        print("exit")
        exit()
    else:
        print(age,"allowed")

for i in range(1,10):
    if i == 5:
        print("exit")
        exit()
    print(i)