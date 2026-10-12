def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def div(num1, num2):
    if num2 == 0:
        return "Error. can't divide by zero."
    else:
        return num1 / num2
history = []

while True:

    operation = (input("Enter mathimathecal operation,quit,history:")).lower()
    if operation == "quit":
        break

    elif operation == "history":
            if len(history) == 0:
                print("no calculation yet.")
            for item in history:
                print(f"{item ["num1"]} {item["operation"]} {item["num2"]} = {item["result"]}")
            continue
  

    try:
        num1 = float(input("Enter your number: "))
        num2 = float(input("Enter your number : "))
        
    except ValueError:
        print("Error. Type real numbers")
        continue

  
       

    if operation == "+":
        result = add(num1,num2)
        print(result)

    elif operation == "-":
        result = sub(num1, num2)
        print(result)

    elif operation == "*":
        result = multiply(num1, num2)
        print(result)

    elif operation == "/":
        result = div(num1, num2)
        print(result)

    
    else:
        print("Unknown operation.")
        continue

    history.append({"num1": num1, "num2": num2, "operation": operation, "result": result})
    
print("Thanks for calculating!")