import random

def generateRandom(number):
    """
    :param number: >=0
    :return: int
    """
    r=random.randint(1,number)
    return r

def main():
    run=True
    num1 = generateRandom(2)
    num2 = generateRandom(3)
    result = num1*num2
    while run:
        ans = input("What is "+str(num1)+" x "+str(num2)+"? ")
        if ans.isdigit():
            if int(ans) == result:
                print("Correct!")
                run = False
            else:
                print("Incorrect! Try again.")
        else:
            print("Answer must")
times = 2
for x in range(times):
    main()
