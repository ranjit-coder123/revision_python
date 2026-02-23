

name = input("Enter yours name: ")
age = int(input("Enter your age :- "))

if age >= 18:
    print(f"hello {name} you are elligible for vote....")#
  

elif age < 18:
    print(f"hello {name} you are not  elligible for vote.....")
else:
    print(f"Invalid input {name}")