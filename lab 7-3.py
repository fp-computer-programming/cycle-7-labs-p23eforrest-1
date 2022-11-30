#Author: EAF 11/28/22
def greeting ():

     'This is a docstring that describes what the function does'

     return("Hello World")

print(greeting)
#executes the function
print(greeting() == "Hello World")
#prints true because the greeting function is the same as the string 'Hello World' 
print(greeting() == "hi")
#prints false because the greeting function is not the same as the string 'Hello World'
print(greeting() == "mrs.")
#prints false because the greeting function is not the same as the string 'Hello World'
print(greeting() == "lebeda")
#prints false because the greeting function is not the same as the string 'Hello World'
 