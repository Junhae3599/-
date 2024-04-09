def arithmetic_ops(op):
    num1 = int(input("첫 번째 정수를 입력하세요. >> "))
    num2 = int(input("두 번째 정수를 입력하세요. >> "))
    return num1, num2, op(num1, num2)
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2

while True:
    c_input = input("연산방법을 입력하세요. >> ")
    if c_input == "end":
        break                                                               # "end"가 입력된 경우 반복을 종료한다.
    elif c_input == "+":
        num1, num2, ret = arithmetic_ops(add)                               #정의된 함수 사용
    elif c_input == "-":
        num1, num2, ret = arithmetic_ops(sub)                               #정의된 함수 사용
    elif c_input == "*":
        num1, num2, ret = arithmetic_ops(lambda num1, num2: num1 * num2)    #익명함수(lambda) 사용
    elif c_input == "/":
        num1, num2, ret = arithmetic_ops(lambda num1, num2: num1 / num2)    #익명함수(lambda) 사용
    elif c_input == "%":
        num1, num2, ret = arithmetic_ops(lambda num1, num2: num1 % num2)    #익명함수(lambda) 사용
    else: 
        print("Invalid opertion")
        continue                                                            #그 외 문자열이 입력된 경우 "Invalid operation"을 출력하고 다시 입력을 받는다.
    print(f"{num1} {c_input} {num2} = {ret}")
print("Exit program")