# Problem 1
# x = ((2**10) + (3**10)) ** 0.5


# Problem 2

x = [1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 4, 1]

# Get the length of  𝑥  in the variable
# l = len(x)

# Change the last element of  𝑥  by 5
# x[-1] = 5

# Add elements 5,6,7,8,9,10 at the end of the list  𝑥
# x.extend([5, 6, 7, 8, 9, 10])

# Extract all odd-indexed elements of 𝑥 in the list 𝑦, and all even-indexed elements of 𝑥 into the list 𝑧
# y = [i for i in range(x.__len__()) if i % 2 == 1]
# z = [i for i in range(x.__len__()) if i % 2 == 0]

# Get all even elements of  𝑥  in the list  𝑦1  and all odd elements of  𝑥  in the list  𝑧1
# y1 = [k for k in x if k % 2 == 1]
# z1 = [k for k in x if k % 2 == 0]

# Replace all odd elements of  𝑥  by 0
# for i in range(x.__len__()):
    # if i % 2 == 1:
        # x[i] = 0

# Find the maximal and minimal elements of  𝑥 , without using the max and min functions
# k = sorted(x)
# print(k[0], k[-1])

# Find the sum of the elements of  𝑥
# sum = sum(x)

# Construct a list  𝐼  consisting of all reciprocals of the elements of  𝑥
# I = [1/k for k in x]

# Find the value of the sum
# k = range(0, 11)
# sum = sum(1/3**i for i in k)
# print(( (1/3) / (1-(1/3)) ) - sum)

# Keep, in the list sec, second letters of all words in the following sentence
# The longest word in any of the major English language dictionaries is pneumonoultramicroscopicsilicovolcanoconiosis.
# sentence_list  = [list("The"), list("longest"), list("word"), list("in"), list("any"), list("of"), list("the"), list("major"), list("English"), list("language"), list("dictionaries"), list("is"), list("pneumonoultramicroscopicsilicovolcanoconiosis")]
# y = [k[1] for k in x]


# Problem 3
word = list("Pneumonoultramicroscopicsilicovolcanoconiosis")

# Find the number of letters in this word
# letters_count = len(word)

# Find the number of letters "o" in this word
# count_o = len([k for k in word if k == "o"])

# Find the number of vowels (ձայնավորներ) in this word
# vowels = len([k for k in word if k == "a" or k == "e" or k == "i" or k == "o" or k == "u" or k == "y"])

# Find how many different letters are there in this word
# y = 0
# x = sorted(word)
# for i in range(x.__len__()-1):
    # if x[i] != x[i + 1]:
        # y = y + 1
# y = y + 1