def print_number(n):
    numbers = range(n)
    for numbers in numbers:
        print(numbers)

def print_even_number(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(number)

def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number}is even")
    else:
        print(f"{number} is odd")

def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number %3 ==0:
            print(f"{number} is divisble by 3")
        elif number%5 == 0:
            print(f"{number} is divisble by 5")
        elif number%7==0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is not divisble by 3,5,7")

def count_down(n):
    x = 0
    while n > x:
        print(n)
        n-=1
def count_down_to_five(n):
    x = 0
    while n>x:
        print(n)
        if n ==5:
            break
        n-=1
def divisible_by_seven(n):
    x=1
    while x <=n:
        x+=1
        if x%7!=0:
            continue
        print(f"{x} is not divisble by 7")

#using while ,continue and if statement ,write a function that prints all the ood numbers btwn 0 and 100
def odd_numbers(n):
    x = 1
    while x <n:
        x+=1
        if x %2==0:
            continue
        print(f"{x} is an odd number")

#write a function named fizzBuzz print numbers divisible by 3 fizz numbers divisble by 5 buzz
#the other numbers print fizzbuzz
def fizz_buzz(n):
    numbers = range(n)
    for number in numbers:
        if number%3==0:
            print(f"fizz")
        elif number%5==0:
            print(f"buzz")
        else:
            print(f"fizzbuzz")








