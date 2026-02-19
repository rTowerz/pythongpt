#x = 10 #int
#x = 3.14 #float
#x = "ten" #str
#name = "Ryan" 
#a, b = 1, 2 # multiple assigment
#a, b = b, a # swap

name = "Ryan"
age = 25
is_student = True

def greet(name, age, is_student):
    if name == "Jose" and age == 25 and is_student:
        return f"Hello, {name}! your age is {age} and you are a student"
    else:
        return "Hello, Guess"
    
    
print(greet(name, age, is_student))

# -------------------------------------

title = "pytHon basics"
print(title.replace("pytHon basics", "Python Basics"))

# -------------------------------------

def bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)

print (round(bmi(68, 1.75), 2))

# -------------------------------------

a, b = 5, 10
a, b = b, a
print(a, b)

# -------------------------------------

name = "Batteries"
qty = 3
price = 5.99

total = qty * price

row = f"{name:15} | {qty:<3} | ${price:>6.2f} | ${total:>6.2f}" 
print(row)

# -------------------------------------

grades = {"math": 90, "cs": 80}

grades["history"] = 88
grades["cs"] = 90

for subject, score in grades.items():
    print(f"{subject}: {score}")

# ---------------------------------------
    
words = ["hi", "to", "python", "hi", "to"]

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)

# ----------------------------------------

score = 90

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(grade)

# -----------------------------------------


s = "  hello  "

if not s.strip():
    print("empty")
else:
    print(s.strip())

# ------------------------------------------
    
total = 0
for n in range(1, 101):
    total += n
print(total)

# ------------------------------------------

words = ["cat", "encyclopedia", "dog"]

for w in words:
    if len(w) > 8:
        print(w)
        break
    else:
        print("None")







