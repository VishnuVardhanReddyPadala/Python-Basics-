# -*- coding: utf-8 -*-
"""Pthon basics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aqujlUhxNLWudGdttOP6yIJOTHSCwU82
"""

my_list = [1, "hello", 3.14]

print(my_list)

my_list = [5, 2, 8, 1]
print(my_list)

# List initialization
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenate the two lists
combined_list = list1 + list2
print(combined_list)

# List initialization
my_list = [1, 2, 3]

# Multiply the list
repeated_list = my_list * 3
print(repeated_list)

t=["a","b","c","d","e","f"]
print(t[1:3])
print(t[:])
print(t[:4])
print(t[:3])
print(t[3:])

# Import the necessary library
from sklearn.linear_model import LinearRegression

# Example data: [hours studied, age, marks]
data = [
    [5, 15, 50],
    [6, 16, 55],
    [8, 17, 65],
    [4, 18, 45],
    [7, 19, 60],
    [3, 20, 40]
]

# Split the data into features (X) and target (y)
X = [item[:2] for item in data]  # Features: hours studied, age
y = [item[2] for item in data]   # Target: marks

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict marks for a new student (age=18, hours studied=6)
new_student = [[6, 18]]
predicted_marks = model.predict(new_student)

# Print the predicted marks
print(f"Predicted marks for a student who studied for 6 hours at age 18: {predicted_marks[0]}")

my_int=42
print("Original Integer:",my_int)

#List Demo
my_list=[1,'hello',3.14,True]
print('Original list:',my_list)
my_list.append('world')
print("List after appending 'world' : ",my_list)
my_list.remove(3.14)
print("List after removing 3.14:",my_list)

#Tuple demo
my_tuple=(1,'apple',3.14,False)
print("Original Tuple:",my_tuple)
#Accessing elements in the tuple
print("First element:",my_tuple[0])
print("Second element:",my_tuple[1])
print("Second element:",my_tuple[-1])

#For loop to print numbers 1 to 5
for i in range(1,6):
  print(i)

#While loop to print numbers 1 to 5
i=1
while i <=5:
  print(i)
  i+=1 #Increment 1 by l

#if condition to check if a number is positive,
number=int(input("Enter a number:"))
if number > 0:
  print("The number is positive.")
elif number < 0:
  print("The number is negative:")
else:
        print("The number is Zero.")

def greet(name):
  print("Hello from function,{name}!")
greet("Alice")