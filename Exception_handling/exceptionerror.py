#syntax errors
#indenation errors
#tabs errors
## exception errors

# print("hello ranjit")


# val =int (input("Enter your number-:"))
# try:
#     print(10/val)          
# except Exception as err:  
#     print(f"sorry there is an error as {err}")
# else:
#     print("good there is no exception")

# finally:
#     print("I will run code no matter what?")

# print("Ok i have done the division......")



# program questions.......

age = int(input("Enter yours age..."))
try:

    if age < 10 or age > 20:
        raise ValueError("Yours age is not Satisfied for addmission... ")
    else:
        print("Welcome to the Club")
except Exception as err:
    print(f"an error occured as {err}")

print("The club will start soon!")





