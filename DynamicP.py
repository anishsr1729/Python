# 1) Sum of Elements in an array
'''def sumOfElements(n, array):
    sum = 0
    for i in range(n):
        sum += array[i]
    return sum
n = 5
array = [1,2, 3, 4, 5]
print(sumOfElements(n, array)) */
'''

# 2) Power Array problem
'''def powerArray(n):
    rev_num = int(str(n)[::-1])
    print(rev_num)
    power = n ** rev_num
    power = str(power)[:5]
    return power
Power = powerArray(12)
print(Power)
'''
# 3) Printing sequence of nos without using loops
'''def printSeq(n):
    if n == 0:
        print(" ")
    else:
        printSeq(n - 1)
        print(n)
printSeq(5)
''' 
# 4) Reversing a string without built in functions
'''def strRev(str):
    str1 = []
    for i in range(len(str)-1, -1, -1):
        str1.append(str[i])
    return ''.join(str1)
print(strRev("geek"))
'''
# 5) Largest no in an array 
'''def largeElement(arr):
    max = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [1, 4, 5, 2]
print(largeElement(arr))
'''
# 6) Deletion of an element based on pos
'''def stackOp(stack, count, pos):
    if not stack:
        print("Stack is empty")
        return stack
    if count == pos:
        stack.pop()
        return stack
    top = stack[-1]
    stc = stack.pop()
    print("The popped element is: ",stc)
    stack = stackOp(stack, count+1, pos)
    stack.append(top)   
    return stack
def prtStack(stack):
    for i in stack:
        print(i)
    
stack = [1, 2, 3, 4, 5]
stc = stackOp(stack, 0, 2)
rev_stc = stc[::-1]
prtStack(rev_stc)
'''

# 7) Tower Of Hanoi
'''def TOH(n, src, dest, aux):
    if n > 0:
        TOH(n-1, src, aux, dest)
        print(f"move disk {n} from {src} to {dest}")
        TOH(n-1, aux, dest, src)

n = int(input("Enter the no of disks: "))    
TOH(n, 'A', 'B', 'C')
print(f"All {n} disks are transferred from A to C")   
'''
# 8) Climbing stairs
'''def climb(n):
    if n <= 2:
        return n
    else:
        print(f"Way {n-1} : ",climb(n-1))
        print(f"Way {n-2} : ",climb(n-2))
        return climb(n-1) + climb(n-2)
        
print(climb(4))
'''
# 9) Stock Market
'''def stockMarket(arr):
    if len(arr) < 2:
        return 0
    min_price = arr[0]
    max_profit = 0
    for i in range(1, len(arr)):
        if (arr[i] < min_price):
            min_price = arr[i]
        else:
            diff = arr[i] - min_price
            max_profit = max(max_profit, diff)
    return max_profit
arr = [7, 1, 5, 3, 6, 4]
print(f"Max Profit is: ",stockMarket(arr))
'''

