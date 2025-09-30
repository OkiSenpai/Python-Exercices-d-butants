


with open("courses.txt", "r") as b:
    a = b.read().splitlines()

n = 1
for i in a:
    print(f"{n}. {i}")
    n +=1
        


