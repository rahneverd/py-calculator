def get_input():
  first_num = input("Enter first number: ")
  second_num = input("Enter second number: ")
  option = input("Select a choice(+, -, *, /): ")
  inputs = {"first": first_num, "second": second_num, "option": option}
  return inputs

def calculate():
  first_num = int(inputs["first"])
  second_num = int(inputs["second"])
  option = inputs["option"]
  if option == "+":
    return first_num + second_num
  elif option == "-":
    return first_num - second_num
  elif option == "*":
    return first_num * second_num
  elif option == "/":
    return first_num / second_num
  else:
    return "Invalid option, try again"

inputs = get_input()
result = calculate()
print(inputs["first"], inputs["option"], inputs["second"], '=', result)