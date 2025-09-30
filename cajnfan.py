list = ["a", "b", "c", "d"]

with open("courses.txt", "w") as f:
     for i in list:
          f.writelines(i + "\n")
  

     
    


with open("courses.txt", "r") as a:
     counter = 1
     for i in a:
         print(counter , i)
         counter += 1
