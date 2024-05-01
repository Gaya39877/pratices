from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-n1','--num1', type=float)
parser.add_argument('-n2','--num2', type=float)
parser.add_argument('-o','--operator', choices=['+','-','*','/'], default='+')

args = parser.parse_args()

num1 = args.num1
num2 = args.num2
operator = args.operator

if (operator == '+'):
    print(num1+num2)
elif(operator == '-'):
    print(num1-num2)
elif(operator == '/'):
    print(num1/num2)
elif(operator == '*'):
    print((num1*num2))