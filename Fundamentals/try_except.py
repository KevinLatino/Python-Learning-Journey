try: 
    number = int(input("Enter a number"))
    division = 100 / number
    print("The result is", division)
except ZeroDivisionError as error:
    print("Error: ", error)
except ValueError as error:
    print("Error: ", error) 