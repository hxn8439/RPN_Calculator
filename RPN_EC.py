#Hamilton Nguyen
#1000538439
#3/28/2021
#python v3.9.1
#calculator program is developed as a stack-based designed.
# ALERT: EXTRA CREDIT PART B WAS PERFORMED NOT PART A.

#Bonus operators
operators = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b),

  #Extra Credit for part B for other arithmetic operations, comparison operations,
  #Logical operations, Bitwise operations, and identity operations.
  "%": (lambda a, b: a % b),
  "^": (lambda a, b: a ^ b),
  "**": (lambda a, b: a ** b),
  "//": (lambda a, b: a // b),
  "<": (lambda a, b: a < b),
  ">": (lambda a, b: a > b),
  "==": (lambda a, b: a == b),
  "!=": (lambda a, b: a != b),
  "<=": (lambda a, b: a <= b),
  ">=": (lambda a, b: a >= b),
  "and": (lambda a, b: a and b),
  "or": (lambda a, b: a or b),
  "not": (lambda a, b: a is not b),
  "is": (lambda a, b: a is b),
  "&": (lambda a, b: a & b),
  "|": (lambda a, b: a | b),
  ">>": (lambda a, b: a >> b),
  "<<": (lambda a, b: a << b)
}

#RPN calculator as declared input.
def rpn_calculator(input):

  #split input into tokens 
  tokens = input.split()
  
  #Declared stack array and set it to zero to prevent IndexError, note disregard one zero in
  #the output compilor.
  stack = [0]

  #Tokens Handling  
  for token in tokens:
    #if statement for handling a token using operators function.  
    if token in operators:
      #pop 2nd argument in the top stack then 1st argument after that.
      argument2 = stack.pop()
      argument1 = stack.pop()
      #organize output of the operator , argument1, and argument2
      output = operators[token](argument1, argument2)
      #append output back onto the stack
      stack.append(output)
    else:
      #append token as int for alternate else case.  
      stack.append(int(token))

  #return pop stack.  
  return stack.pop()

#declare file lines array.
file_lines = []

#open file using read for text file.
with open('input_RPN_EC.txt', 'r') as f:
    #execute the readlines function and store it in the file lines array.
    file_lines = f.readlines()

#For loop statement using each row in file lines array.
for row in file_lines:
    #print statement for the outputted rpn values.
    print(rpn_calculator(f'{row}'))