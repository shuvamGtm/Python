'''Create a simple calculator by taking two numbers from user that can perform orthemetic
operations like addition, subtraction,multiplication, division, exponemtial.'''

input1=int(input("Enter 1st number: "))
input2=int(input("Enter 2nd number: "))

operator1=''

while operator1 not in ('+' ,'-','/','**','*','%'):
    operator1=input('''Choose a arthemetic operator from the following options:
    1)+ 
    2)-
    3)*
    4)/
    5)**
    6)%\n''')
        
if operator1=='+':
    print(input1+input2)
elif operator1=='-':
    print(input1-input2)
    print(input1/input2)
elif operator1=='**':
    print(input1**input2)
elif operator1 == '*':
    print(input1*input2)
elif operator1== '%':
    print(input1%input2)


