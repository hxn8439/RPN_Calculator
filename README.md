# RPN_Calculator

# Purpose

Program was developed in Python to create a simple calculator that accepts Reverse Polish Notation (RPN) and displays the final answer.

# requirements:
1. It only accepts 4 operators “+”, “-“, “*”, “/”.
2. Input numbers will be single digits. 
3. The input will be in postfix notation.  
4. The input will be provided in a text file called input_RPN.txt.
5. Your program should not ask the user for any input. 
6. There will be one RPN expression in each line. 
7. Your code should be able to read the file and print the result for each RPN in a new line.

Example of RPN: 4 2 + and your output should be 6. This is a simple expression. More complex algebraic notations will be used to test your program like the one below.

Example algebraic notation: ( 4 + 2 * 5 ) / ( 1 + 3 * 2 )

Translated into RPN: 4 2 5 * + 1 3 2 * + /

Note: - The code should be able to read the input file from the same folder (which has your .py file). 

A separate program  was written that can input an algebraic expression and convert it to RPN and then evaluate the RPN. Print the RPN and the result in separate lines. The file is name as RPN_EC.py. The input file name will be RPN_EC.txt and it will have algebraic expressions. Note that it has more operators (unary subtraction, or modulo division, etc.)

