def get_evens(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens

my_nums = [1,2,3,4,5,6,7,8,9,10]
print(get_evens(my_nums))