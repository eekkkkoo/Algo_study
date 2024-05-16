# baekjoon 10828
class Stack:
    def __init__(self):
        self.stk = [None] * 1024
        self.stk_num = 0
    
    def push(self, X):
        self.stk[self.stk_num] = X
        self.stk_num += 1
    
    def pop(self):
        if self.stk_num == 0:
            return '-1'
        else:
            last = self.stk[self.stk_num-1]
            self.stk[self.stk_num-1] = None
            self.stk_num -= 1
            return last
            
    def size(self):
        return self.stk_num
    
    def empty(self):
        if self.stk_num == 0:
            return '1'
        else:
            return '0'
    
    def top(self):
        if self.stk_num == 0:
            return '-1'
        else:
            return self.stk[self.stk_num-1]

def ord_f(order):
    if order[0] == 'pop':
        return print(s.pop())
    elif order[0] == 'size':
        return print(s.size())
    elif order[0] == 'empty':
        return print(s.empty())
    elif order[0] == 'top':
        return print(s.top())
    elif order[0] == 'push':
        return s.push(int(order[1]))
    else:
        return print('error')

n = int(input('input number of order: '))
s = Stack()
ord_num = 0
while ord_num < n:
    order = input().split()
    ord_num += 1
    ord_f(order)
