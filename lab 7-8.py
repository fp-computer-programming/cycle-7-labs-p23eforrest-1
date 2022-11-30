#Author: EAF 11/28/22

def min(arr):
    arr.sort()
    #sorts the array from least to greatest
    return arr[0]
    #finds first number of array(smallest number) and returns it

#first function which finds lowest number from the inputted array

def max(arr):
    arr.sort()
    #sorts the array from least to greatest
    return arr[-1]
    #finds last number of array(largest number) and returns it

#second function which finds the highest number from the inputted array

def both(arr):
    smallest = min(arr)
    #setting the min function as a smallest variable since it returns the smallest number
    largest = max(arr)
    #setting the max function as a largest variable since it returns the largest number
    return(smallest, largest)
    #returns smallest and largest number

#third function which returns both the highest and lowest numbers of the array in the same statement

print(both([1.2,2,3,4,5,6,7,8.5]))
