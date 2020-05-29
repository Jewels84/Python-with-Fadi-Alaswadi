#An array with  its elements has to be written like this 
subjects=['Arabic','Maths','English','Reliegon','History']
print(subjects)  #DO NOT put the barckets as it will print the word subject 
#instead of the elements

#NOTE the orders of the elements in the arrya starts with 0,1,2
print(subjects[1])

#To add/delete an element use append/pop
subjects.append('Science')
print(subjects)
# subjects.pop(3)
# print(subjects)

print(subjects[1:2])
#honestly I didint understand why its going to print only1