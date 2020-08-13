### FizzBuzz Challenge ###

## Write a program that outputs the string representation of numbers from 1 to n.
## But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
## For numbers which are multiples of both three and five output “FizzBuzz”. ###

# def FizzBuzz(self, n: int) -> list[str]:
# range(1, n+1) <--- loop through this
# x15 (needs to be first because it would catch at the other two as well.)
# x3
# x5

# Solution 1 #
def fizzBuzz(self, n: int) -> List[str]:
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))
    return result

# Solution 2 #
def fizzBuzz(self, n):
    self.numbers = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            self.numbers.append('FizzBuzz')
        elif num % 3 == 0:
            self.numbers.append('Fizz')
        elif num % 5 == 0:
            self.numbers.append('Buzz')
        else:
            self.numbers.append(str(num))
    return self.numbers
