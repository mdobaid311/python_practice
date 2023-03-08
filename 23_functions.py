def average(num1, num2, num3, name="obaid"):
    total = num1 + num2 + num3
    print(total)
    average = total / 3
    print(f"{name}'s average is", average)


# average(12,31,12)

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result

# print(factorial(3))


def factorial_recursive(num):
    if num == 1:
        return 1
    else:
        return num * factorial_recursive(num-1)

# print(factorial_recursive(31))


def greatest_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

# print(greatest_of_three(12,2,3))


def sum_of_numbers(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    return sum

print(sum_of_numbers(3))
