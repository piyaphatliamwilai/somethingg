import time

# introduce

print("Hello, this is really bad program. Please check the answer if it was wrong or correct!")
print(":)")

# input

number = int(input("Put the number -> "))
divideMinimum = int(input("Put the minimum of divisible number you want -> "))
divideMaximum = int(input("Put the maximum of divisible number you want -> "))

# calculating time / main

divideNumber = divideMinimum
while 3 > 2:
    outputCalculate = number
    outputCalculate = outputCalculate / divideNumber
    numberChecker = (outputCalculate.is_integer())
    if (numberChecker == True):
        print(divideNumber)
        print("--")
        print(outputCalculate)
        print("--")
    elif (numberChecker == False):
        time.sleep(0.000000001)
    divideNumber = divideNumber + 1
# check divideNumber

if (divideNumber == divideMaximum):
    print("Program finished, check the answer above 1 by 1.")
    while 3 > 2:
        time.sleep(0.1)
