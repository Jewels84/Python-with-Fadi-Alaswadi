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

#Writing the FOR LOOP
for x in subjects:
    #print(x)
    print(x,x,x)

no=[1,2,3,4,5 ,6]
print(no)

#there is some errors I will fix it later on
for x,y in no,subjects:
    print(x,y)