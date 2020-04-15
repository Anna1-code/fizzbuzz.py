num =int(input("what is your number?"))
if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print(f"{num}is not divisible by 3 and 5")

