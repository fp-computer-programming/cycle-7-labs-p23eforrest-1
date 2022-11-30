#Author: EAF 11/28/22

def find_sum(num1,num2):
    #creates function named 'find_sum' and sets the parameters of variables num1 and num2
     num_sum = num1 + num2
     #making a variable in the function that adds the variables num1 and num2
     return(num_sum)
     #returns num_sum

my_sum = find_sum(111,222)
#calls the function to find the sum
print(my_sum)
#prints the variable my_sum

print(find_sum(103,230) == 333)
#prints true because the sum of these two numbers equals 333
print(find_sum(10,10) == 100)
#prints false because the sum of these two numbers does not equal 100
print(find_sum(70,1) == 71)
#prints true because the sum of these two numbers equals 71
print(find_sum(20.5,20) == 40.5)
#prints true because the sum of these two numbers equals 40.5