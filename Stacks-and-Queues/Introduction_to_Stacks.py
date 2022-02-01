def isempty(stack):
    return len(stack) == 0

def push(stack, item):
    global top  
    stack.append(item)
    top += 1

def pop(stack):
    global top
    if isempty(stack) == True:
        return 'Underflow'
    else:
        item = stack.pop()
        if len(stack) == 0:
            top = -1
        else:
            top -= 1 
        return item

def peek(stack):
    global top 
    if isempty(stack) == True:
        return 'Underflow'
    else:
        return stack[top]

def display(stack):
    global top
    if isempty(stack):
        print('stack empty')
    else:
        print(stack[top], ' <-- top')
        for index in range(top - 1, -1, -1):
            print(stack[index])

stack = []
top = -1
while True:
    print('STACK OPERATIONS') 
    print('1.Push') 
    print('2.Pop') 
    print('3.Peek') 
    print('4.Display Stack') 
    print('5.Exit')
    option = int(input('Enter your choice (1-5):')) 
    if option == 1:
        item = int(input('Enter item:')) 
        push(stack,item)
    elif option == 2:  
        item = pop(stack) 
        if item == "Underflow": 
            print("Underflow!Stack is empty!")
        else: 
            print("Popped item is", item)
    elif option == 3: 
        item = peek(stack) 
        if item == "Underflow": 
            print("Underflow!Stack is empty")
        else: 
            print("Topmost item is", item)
    elif option == 4: 
        display(stack)
    elif option == 5: 
        break
    else: 
        print('Invalid choice')