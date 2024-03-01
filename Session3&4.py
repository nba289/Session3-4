name = input("what is your name?")
age = input("How old are you? ")
#print("Hello, ", name, "!", sep="")
try:
    age = int(age)
    birth_year = 2024 - age
    print(name, ", you were born in ", birth_year, ".", sep="")
    number = input("give me a number to divide the age ")
    number = int(number)
    print(age / number)
except ValueError:
    print("Write a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
except:
    print("You messed up something else!")
else:
    print("All good")
    print("Now leave me alone!")