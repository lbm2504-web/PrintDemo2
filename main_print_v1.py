#1
print("Hello world!")

name = "Alice"
age = 25
score = 95.5

#2
print("Name:", name, "Age:", age, "Score", score)

#3
print(f"My name is {name}, I am {age} years old, score: {score}")

#4
print("My name is {}, I am {} years old, score: {}".format(name, age, score))
print("My name is {0}, age {1}, score {2}".format(name, age, score))
print("Score with 2 decimals {:.2f}".format(score))

#5
print("Name: %s, Age: %d, Score: %.1f"%(name, age, score))

#6
print("This is line 1\nThis is line 2")

#7
print("Hello", end="")
print("World!")

#8
print("2025", "09","23", sep="-")

#9
data = {"name": name, "age": age, "score": score}
print("Data", data)

#10
print(f"Next year age: {age+1}")
print(f"Score (rounded): {round(score)}")

#11
print(f"""
Student Info:
 - Name : {name}
 - Age  : {age}
 - Score: {score:.2f}
 """)

