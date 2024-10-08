
file = open('readline.txt','w')
file.write('''Hi my name is saugat and I live in australia
I am 22 years old 
I am studying Bachelor of information Technology
I am interested in Data science''')
file.close()

file=open('readline.txt','r')
text = file.read()
print(text)

#using readline function
file = open('readline.txt','r')
while True:
    line = file.readline()
    if not line:
        break
    print(line)

 

#write line

file2= open('myfile2.txt','w')
write = ['45,55,65\n', '45,67,56\n', '77,67,87\n']
file2.writelines(write)
file2.close()

file2 = open('myfile2.txt','r')
text = file2.read()
print(text)
file2.close()


newfile = open('myfile2.txt','r')
i = 0
while True:
    i = i + 1
    line = newfile.readline()
    if not line:
        break
  
    marks1 = line.split(",")[0]
    marks2 = line.split(",")[1]
    marks3 = line.split(",")[2]
    print(f"The mark of student {i} in Maths is {marks1}")
    print(f"The mark of student {i} is in Science {marks2}")
    print(f"The mark of student {i} is Physics {marks3}")
   
    print(line)
