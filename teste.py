list = [8,5,6,96,2,1,4,5]


for i in range(len(list)):
   
    
   
    for a in range( len(list)):
        if list[i] < list[a]:
            temp = list[i]
            list[i] = list[a]
            list[a] = temp
      
    
print(list)