#Author: EAF 11/29/22

def num_sorting(one, two, three, four,):
    #creates list with these 8 variables
    numbers = [one, two, three, four,]
    #creates a variable containing these 8 variables in an array
    numbers.sort()
    #sorts numbers from least to greatest
    return("Lowest number is " + str(numbers[0]) + ". Highest number is " + str(numbers[-1]) + ".")

print(num_sorting(5, 8, 1, 9) == "Lowest number is 1. Highest number is 9.")
#prints true

def wordywords(one, two, three, four):
    words = [one, two, three, four]
    #creates variabel and puts the fucntion variables in an array
    length = [len(one), len(two), len(three), len(four)]
    #grabs the length of each variable and puts it in a new variable
    return(words, length)

print(wordywords("My", "name", "is", "Ethan") == (["My", "name", "is", "Ethan"], [2, 4, 2, 5]))
#test case: prints true

def multiplying(one, two, three, four):
    nums = [int(one) * 2, int(two) * 2, int(three) * 2, int(four) * 2]
    #converts the function variables into integers and multiplies them by 2
    return(nums)

print(multiplying(10, 20, 30, 40) == [20, 40, 60, 80])
#test case: prints true

def oddies_evenies(one, two, three, four):
    nums = [int(one), int(two), int(three), int(four)]
    #converts to integers so we can multiply
    if(nums[0]%2 == 0 and nums[1]%2 == 0 and nums[2]%2 == 0 and nums[3]%2 == 0):
        #this math confirms that the numbers are even
        return("even")
    elif(nums[0]%2 != 0 and nums[1]%2 != 0 and nums[2]%2 != 0 and nums[3]%2 != 0):
        #this math confirms that the numbers are odd
        return("odd")
    else:
        #if the numbers are neither fully even or odd, it will print this
        return("mixed")

print(oddies_evenies(80, 6, 26, 54) == "even")
print(oddies_evenies(91, 23, 21, 11) == "odd")
print(oddies_evenies(301, 960, 74, 803) == "mixed")
#test cases: all print true