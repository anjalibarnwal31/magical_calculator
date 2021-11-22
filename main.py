import re

print("Our magical calculator")
print("type 'quit' to exit\n")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation =""
    if previous == 0:
        equation = input("enter equations:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
      print("good bye human")
      run = False
    else:
      equation = re.sub('[a-zA-Z,.:()" "]', '',equation)

    if previous == 0:
      previous= eval(equation)
    else:
      previous = eval(str(previous)+equation)

while run:
    perform_math()
