#!/usr/bin/env python3
#Kevin Wong
#kmw396 - 14240214
#November 15, 2018
#Assignment 2: Convert Infix Expressions to Postfix then Calculate in Python 

import sys
#Interface Class for a Stack
#Only allows access to the stack commands of the built in list
class Stack:
	#Create a New Empty Stack
    def __init__(self):
        self.__S = []
	#Display the Stack
    def __str__(self):
        return str(self.__S)
    #Returns itself
    def isEmpty(self):
        return self.__S == []
	#Add a new element to top of stack
    def push(self,x):
        self.__S.append(x)
	#Remove the top element from stack
    def pop(self):
        return self.__S.pop()
	#See what element is on top of stack
    def peek(self):
        return self.__S[0]
	#Leaves stack unchanged
    def top(self):
        return self.__S[-1]
    #Stack Size
    def size(self):
        return len(self.__S)

#Function for converting Infix Expressions to Postfix
def infix2postfix(expr):
    #Operator Order of Operations
    operator = {}
    operator["+"] = 3
    operator["-"] = 3
    operator["%"] = 2
    operator["*"] = 2
    operator["/"] = 2
    operator["("] = 1
    #Initalize Stack class
    stack = Stack()
    #Postfix expression list
    postfixList = []
    #Split expression, add to token list, and append right peren, insert left peren
    tokenList = expr.split()
    tokenList.append(')')
    tokenList.insert(0, '(')
    
    #Iterate over split expression
    for token in tokenList:
        #Checks for operands, appends to postfix expression
        if token.isnumeric():
            postfixList.append(token)
        #Checks for left paren, push to stack
        elif token == '(':
            stack.push(token)
        #Checks for right paren, removes operators from stack, appends to postfix expression until left paren is encountered. Discards left paren.
        elif token == ')':
            topToken = stack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = stack.pop()
        #Checks if operator is encountered, removes operators from stack and appends to postfix expression while its greater or equal than the current token. Pushes current toekn to stack 
        else:
            while (not stack.isEmpty()) and (operator[stack.peek()] >= operator[token]):
                postfixList.append(stack.pop())
            stack.push(token)
            
    #Pops all operators from the stack
    while not stack.isEmpty():
        postfixList.append(stack.pop())
    #Returns postfix expression
    return postfixList

#Function calculates postfix expressions and returns final value to stack
def evalPostfix(postfix):
    #Initalize Stack
	stack = Stack()
    #Iterates over postfix expression. Runs through each operator.
	for operator in postfix:
		if operator == '+':
			x = stack.top()
			stack.pop()
			y = stack.top()
			stack.pop()
			total = int(x)+int(y)
			stack.push(total)
		elif operator == '-':
			x = stack.top()
			stack.pop()
			y = stack.top()
			stack.pop()
			total = int(y)-int(x)
			stack.push(total)
		elif operator == '*':
			x = stack.top()
			stack.pop()
			y = stack.top()
			stack.pop()
			total = int(x)*int(y)
			stack.push(total)
		elif operator == '/':
			x = stack.top()
			stack.pop()
			y = stack.top()
			stack.pop()
			total = int(y)/int(x)
			stack.push(total)
		elif operator == '%':
			x = stack.top()
			stack.pop()
			y = stack.top()
			stack.pop()
			total = int(y)%int(x)
			stack.push(total)
		else:
			stack.push(operator)
	return stack.top()

def main(args):
    if len(args) < 2: #read stdin
        expression = sys.stdin
    else:
        expression = open(args[1])
    
    print("Welcome to Postfix Calculator")
    print("Enter exit to quit")

    #Expression Input
    valid = False
    while not valid:
        expression= input("Enter Expression:\n")
        if expression.lower() == 'exit':
            exit()
        #Runs through Functions and Prints
        expr = infix2postfix(expression)
        print("Result:",evalPostfix(expr))
    return 0

if __name__=="__main__":
    sys.exit(main(sys.argv))