# This function adds two numbers
from cgi import print_directory


def add(x,y):
    return x+y

#This function substracts two number
def substract(x,y):
    return x-y

# This function multiple two function
def multiply(x,y):
    return x*y

#This function divide two function
def divide(x,y):
    return x/y

print("select operation.")
print("1.Add")
print("2.substract")
print("3.multiply")
print("4.divide")

while True:
    choice=input("entre chooice(1/2/3/4):")

    if choice in ('1','2','3','4'):
        try:
            num1=float(input("entre first number:"))
            num2=float(input("entre second number:"))
        except ValueError:
            print("invalid input. please entre a nember.")
            continue
        if choice =='1':
            print(num1,"+", num2, "=",add(num1,num2))

        elif choice =='2':
            print(num1,"-", num2, "=",substract(num1,num2))

        elif choice =='3':
            print(num1,"*", num2, "=",multiply(num1,num2))

        elif choice =='4':
            print(num1,"/", num2, "=",divide(num1,num2))  


        next_calculation = input("let's do next calculation? (yes/no):")
        if next_calculation =="no":
            break

    else:
        print("invalid input")                             
                

