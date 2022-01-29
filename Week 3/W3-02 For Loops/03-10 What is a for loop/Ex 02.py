def square(n):
    return n*n
print(square(10))

def sum_squares(x):
    sum = 0
    for z in range(x):
        sum += square(z)
    return sum

print(sum_squares(10)) # Should be 285
# print(sum_squares(3)) # should be 5
