"""

Project Euler - Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

num_range = int(input("\n>> "))
unique_amicable = set()


def is_checked(num):
    if num in unique_amicable:
        return 1
    else:
        return 0

def is_amicable(num1, num2):
    d1 = find_divisor_sum(num1)
    d2 = find_divisor_sum(num2)

    if ((d1 == num2) and (d2 == num1)):
        return 1
    else:
        return 0

def find_amicable_numbers(num_range):

    amicable_sum = 0

    for i in range(201, num_range):
        for j in range(202, num_range):
            if ((is_checked(i)) or (is_checked(j)) or (i == j)):
                continue
            if (is_amicable(i, j)):
                unique_amicable.update([i, j])

    for i in unique_amicable:
        amicable_sum += i

    print(amicable_sum)

    return 0
  

def find_divisor_sum(num):

    sum = 0

    for i in range(1, (int(num/2) + 1)):
        if ((num % i) == 0):
            sum += i

    return sum

find_amicable_numbers(num_range)
