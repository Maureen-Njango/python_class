def add(x,y):
    results = x+y
    return results
def substract(m,y):
    results = m-y
    return results
def divide(m,u):
    results = m/u
    return results
def multiply(m,y):
    results = m*y
    return results
def remainder(m,y):
    results = m%y
    return results
def power_of(m,y):
    results = (m**y)
    return results
def sum(*numbers):
    total = 0 
    for number in numbers:
        total += number
    return total

def multiply_many(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

def create_sentence(**words):
    print(words)
    sentence = " "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence

def sum_and_greet(*args, **kwargs):
    total = 0
    for x in args:
        total+= x
        f = kwargs["first_name"]
        l = kwargs["last_name"]
    greetings = f"Hello {f} {l} the sum of your number is total {total}"
    return greetings


   