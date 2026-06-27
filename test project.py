print("Students Scores")
scores = {
    "Rahul":int(input("Enter your score: ")),
    "Ram":int(input("Enter your score: ")),
    "Shivaansh":int(input("Enter your score: ")),
    "Vihaan":int(input("Enter your score: ")),
    "Avyaan":int(input("Enter your score: "))
}
Sum = 0
for i in scores.values():
    Sum += i
Average = Sum // 5
print(f"The Average marks are {Average}")
highest = max(scores.values())
lowest = min(scores.values())
for name,score in scores.items():
    if highest == score:
        print(f"the highest score is {score} and scored by {name}")
    if lowest == score:
        print(f"the lowest score is {score} and is scored by {name}")

student = input("Enter your students name: ")
print(scores.get(student,"Your student is not found"))