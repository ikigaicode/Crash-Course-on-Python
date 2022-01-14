def sum_divisors(n):
    if n == 0:
        return 0
    sum = 0

    # Return the sum of all divisors of n, not including n
    counter = 1
    while counter < n:
        if n % counter == 0:
#            print("This number is a factor, " + str(counter))
            sum += counter
        counter += 1

    return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
