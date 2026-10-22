# Fizz -> 3, Buzz -> 5, FizzBuzz -> 3 y 5
def fizzbuzz(i):
    if (i % 3 == 0):
        if (i % 5 == 0):
            return "FizzBuzz"
        return "Fizz"
    elif (i % 5 == 0):
        return "Buzz"
    else:
        return str(i)