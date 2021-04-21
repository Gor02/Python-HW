# Problem 1

# Construct a Dictionary cities_AM that corresponds to largest 5 Armenian cities their population, say, for Yerevan,
# the population is 1077.6 (in thousands).

# cities_AM = {"Yerevan": 1077.6,
             # "Vagharshapat": 46.4,
             # "Kapan": 42.5,
             # "Vanadzor": 79.3,
             # "Gyumri": 114.5
# }

# Print the names of cities

# for i in cities_AM:
    # print(i)

# Print the sum of population in largest 5 Armenian cities

# s = 0
# for i in cities_AM.values():
    # s += i
# print(s)

# Get the name of the second largest (by population) city in Armenia (not by a hand, of course ☺)

# l = []
# for i in cities_AM.values():
    # l.append(i)
# for j in range(len(l)):
    # for k in range(len(l)):
        # if l[j] > l[k]:
            # l[j], l[k] = l[k], l[j]
# for i in cities_AM:
    # if cities_AM[i] == l[1]:
        # print(i)

# Add the 6th city with its population to the dictionary

# cities_AM["Hrazdan"] = 40.4

# Find information about the surface areas of cities, and update dictionary to include tuples (population, area) for
# each city.

# area = [223, 40, 36, 32, 54, 152]
# key = [i for i in cities_AM.keys()]
# cities_AM.update({key[i]: (cities_AM[key[i]], area[i]) for i in range(len(cities_AM))})

#Construct a similar dictionary cities_GE for Germany 2 largest cities, and create a new Dictionary,
# with keys "Armenia", "Germany", and values as the constructed dictionaries

# cities_GE = {"Berlin": 3.275,
             # "Hamburg": 1.686
# }

# countries = {"Armenia": cities_AM,
             # "Germany": cities_GE
             # }

# Problem 2

# Consider the list x = [1, -2, 3, 9, 0, 1, 3, 2, -2, -4, 1, -3] . Construct two lists, x_neg and x_pos containng,
# correspondingly, all negative and all positive elements of x in the same order.
# Construct also lists ind_neg and ind_pos which will contain the indices of all negative and positive elements of x,
# respectively.

# x = [1, -2, 3, 9, 0, 1, 3, 2, -2, -4, 1, -3]

# x_neg = [i for i in x if i < 0]
# x_pos = [i for i in x if i > 0]

# ind_neg = [i for i in x if x[i] < 0]
# ind_pos = [i for i in x if x[i] > 0]

# Find the sum 1+3+5+...+101

# sum_ = 0
# for i in range(1, 102, 2):
    # sum_ += i

# Calculate the sum 1+1/2+3+1/4+5+1/6+...+99+1/100

# sum_ = 0
# for i in range(101):
    # if not i % 2:
        # sum_ += i
    # else:
        # sum_ += 1 / i

# Calculate the semifactorial  20!!

# factorial = 1
# for i in range(2, 21, 2):
    # factorial *= i

# Calculate the sum

# def f(x):
    # fact = 1
    # for i in range(1, x):
        # fact *= i
    # return fact

# sum_ = 0
# for i in range(20):
    # sum_ += (-1) ** i / f(i)

# Calculate the sum

# s_n = 0
# n = 0
# while True:
    # for i in range(n + 1):
        # s_n += i / 2 ** i
    # if abs(s_n - 2) <= 0.001:
        # print(n)
        # break
    # n += 1
    # s_n = 0

# Given a list of real numbers, find the maximum element of that list, without using any built-in Python max function

# l = [1, 2, 3, 4, 5, 6]
# max_element = l[0]
# for i in l:
    # if i > max_element:
        # max_element = i

# Given a list of arbitrary reals, write a sorting algorithm to sort the list in the increasing order,
# without using the Python built-in sorting algorithms. You can implement quicksort,
# bubble sort or any other well-known algorithm, or just write a simple (maybe non-effective) algorithm.

# for j in range(len(l)):
    # for k in range(len(l)):
        # if l[j] > l[k]:
            # l[j], l[k] = l[k], l[j]

# Define the following function in Python

# def f(x):
    # if x < 0:
        # return -1
    # elif x <= 0 and x <= 5:
        # return 4
    # else:
        # return 9

# Define the following function in Python

# def g(x):
   # if x < 0 and x > 10:
        # return 1
    # else:
        # return 0

# Write a function of natural variable  𝑛  that will return the  𝑛 -the Fibonacci number

# def fibo(x):
    # a = 0
    # b = 1
    # while a <= x:
        # print(a)
        # c = a + b
        # a = b
        # b = c