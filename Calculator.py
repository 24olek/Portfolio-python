choice1 = None
choice2 = None
choice3 = None
choice4 = None
result = None
number1 = None
number2 = None
while choice1 != "0":
    print("""Welcome to calculating program.
          1. Start calculating.
          0. Exit program.""")
    choice1 = input()
    if choice1 == "1":
        while choice2 != 0:
            print("To back to the prevorious menu introduce \"0\"")
            choice2 = int(input("Introduce number: "))
            if choice2 == 0:
                break
            number1 = choice2
            choice2 = int(input("Introduce factor: "))
            number2 = choice2
            choice3 = int(input("""1. Addition.
2. Subtraction.
3. Muliptlication.
4. Division.\n"""))
            if choice3 == 1:
                result = number1 + number2
                print("Result: ", result)
            elif choice3 == 2:
                
                result = number1 - number2
                print("Result: ", result)
            elif choice3 == 3:
                result = number1 * number2
                print("Result: ", result)
            elif choice3 == 4:
                result = number1 / number2
                print("Result: ", result)
            elif choice3 == 0:
                break
            else:
                print("Chose operation from menu.")
                break

            while choice4 != 0:
                choice4 = int(input("""1. Addition.
2. Subtraction.
3. Muliptlication.
4. Division.
0. New operation\n"""))

#Used number1 as variable in loop                
                number1 = None
                if choice4 == 1:
                    number1 = int(input("Introduce factor: "))
                    result += number1
                    print("Result: ", result)
                elif choice4 == 2:
                    number1 = int(input("Introduce factor: "))
                    result -= number1
                    print("Result: ", result)
                elif choice4 == 3:
                    number1 = int(input("Introduce factor: "))
                    result *= number1
                    print("Result: ", result)
                elif choice4 == 4:
                    number1 = int(input("Introduce factor: "))
                    result /= number1
                    print("Result: ", result)
                elif choice4 == 0:
                    break
                else: print("Choice option from menu.")

            choice4 = None

                
                
            
        
            
            



    choice2 = None
    choice3 = None
    choice4 = None
    result = None
    number1 = None
    number2 = None
            
