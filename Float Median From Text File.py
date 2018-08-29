# Opens and reads the file, then splits the numbers
numbers_file = open("numbers.txt").read().split()

# Makes numbers in list float
float_list = [float(numbers) for numbers in numbers_file]

# Returns the number of items in this list
lenght = len(float_list)


# Two variables, both are 0 at the beginning
summarize = 0
numbers_in_list= 0

# For loop to summaraize numbers in list
for numbers in float_list:
    summarize += float_list[numbers_in_list]
    numbers_in_list += 1

# Median = summarized numbers / how many numbers were in the list
median = summarize/lenght
print(median)
