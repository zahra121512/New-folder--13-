num1 = float(input("please enter the first value :"))
num2 = float(input("please enter the second value :"))

while(num2 != 0 ):
    temp = num2
    num2 = num1 % num2
    num1 = temp 

hcf = num1
print("hcf of num 1 and num2 is" , hcf)
