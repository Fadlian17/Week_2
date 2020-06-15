# frequent number and grade
# list
numbers = [1, 2, 3, 4, 5, 6, 6, 8, 8, 6, 9]
grades = [87.5, 88.5, 60.5, 90.5, 88.5]


def most_frequent(List):
    counter = 0
    numgrade = List[0]

    for i in List:
        list_freq = List.count(i)
        if (list_freq > counter):
            counter = list_freq
            numgrade = i

    return numgrade


print("Most Frequent Number is: ", (most_frequent(numbers)))
print("Most Frequent Grade is: ", (most_frequent(grades)))
